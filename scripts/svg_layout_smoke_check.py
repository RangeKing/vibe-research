#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


Box = tuple[float, float, float, float]
TextBox = tuple[int, str, float, float, float, float]


def local_name(tag: str) -> str:
    return tag.split("}", 1)[-1]


def parse_float(value: str | None) -> float | None:
    if value is None:
        return None
    match = re.match(r"\s*(-?\d+(?:\.\d+)?)", value)
    if not match:
        return None
    return float(match.group(1))


def parse_viewbox(root: ET.Element) -> tuple[float, float, float, float] | None:
    viewbox = root.attrib.get("viewBox")
    if viewbox:
        parts = [float(p) for p in re.split(r"[,\s]+", viewbox.strip()) if p]
        if len(parts) == 4:
            return tuple(parts)  # type: ignore[return-value]

    width = parse_float(root.attrib.get("width"))
    height = parse_float(root.attrib.get("height"))
    if width is not None and height is not None:
        return (0.0, 0.0, width, height)
    return None


def text_content(node: ET.Element) -> str:
    return "".join(node.itertext()).strip()


def font_size(node: ET.Element) -> float:
    size = parse_float(node.attrib.get("font-size"))
    return size if size is not None else 16.0


def estimated_width(text: str, size: float) -> float:
    # Conservative estimate for Arial-like scientific SVG text.
    return len(text) * size * 0.58


def has_wrapping(node: ET.Element) -> bool:
    return any(local_name(child.tag) == "tspan" for child in node)


def parse_rect(node: ET.Element) -> Box | None:
    x = parse_float(node.attrib.get("x")) or 0.0
    y = parse_float(node.attrib.get("y")) or 0.0
    width = parse_float(node.attrib.get("width"))
    height = parse_float(node.attrib.get("height"))
    if width is None or height is None:
        return None
    return (x, y, x + width, y + height)


def find_panel_boxes(root: ET.Element, canvas: Box) -> list[Box]:
    canvas_left, canvas_top, canvas_right, canvas_bottom = canvas
    canvas_w = canvas_right - canvas_left
    canvas_h = canvas_bottom - canvas_top
    panels: list[Box] = []
    for node in root.iter():
        if local_name(node.tag) != "rect":
            continue
        box = parse_rect(node)
        if box is None:
            continue
        left, top, right, bottom = box
        width = right - left
        height = bottom - top
        fill = node.attrib.get("fill", "").lower()
        stroke = node.attrib.get("stroke", "").lower()
        if width < 180 or height < 120:
            continue
        if width >= canvas_w * 0.95 and height >= canvas_h * 0.95:
            continue
        if fill not in {"#ffffff", "white"}:
            continue
        if stroke in {"", "none"}:
            continue
        panels.append(box)
    return panels


def point_inside(box: Box, x: float, y: float, pad: float = 0.0) -> bool:
    left, top, right, bottom = box
    return left - pad <= x <= right + pad and top - pad <= y <= bottom + pad


def box_area(box: Box) -> float:
    left, top, right, bottom = box
    return max(0.0, right - left) * max(0.0, bottom - top)


def assign_panel(panels: list[Box], x: float, y: float) -> Box | None:
    containing = [box for box in panels if point_inside(box, x, y, pad=2.0)]
    if not containing:
        return None
    return min(containing, key=box_area)


def check_svg(path: Path) -> list[str]:
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        return [f"{path}: invalid SVG/XML: {exc}"]

    viewbox = parse_viewbox(root)
    if viewbox is None:
        return [f"{path}: missing width/height or viewBox"]

    min_x, min_y, width, height = viewbox
    max_x = min_x + width
    max_y = min_y + height
    canvas = (min_x, min_y, max_x, max_y)
    margin = max(12.0, min(width, height) * 0.01)
    warnings: list[str] = []
    panels = find_panel_boxes(root, canvas)

    text_nodes = [node for node in root.iter() if local_name(node.tag) == "text"]
    if not text_nodes:
        warnings.append(f"{path}: no text nodes found; verify labels after raster render")

    boxes: list[TextBox] = []
    for idx, node in enumerate(text_nodes, start=1):
        content = re.sub(r"\s+", " ", text_content(node))
        if not content:
            continue
        x = parse_float(node.attrib.get("x"))
        y = parse_float(node.attrib.get("y"))
        size = font_size(node)
        anchor = node.attrib.get("text-anchor", "start")
        approx_w = estimated_width(content, size)

        if x is None or y is None:
            warnings.append(f"{path}: text #{idx} lacks explicit x/y: {content[:80]!r}")
            continue

        if len(content) > 75 and not has_wrapping(node):
            warnings.append(
                f"{path}: long unwrapped text #{idx} ({len(content)} chars): {content[:100]!r}"
            )

        if anchor == "middle":
            left = x - approx_w / 2
            right = x + approx_w / 2
        elif anchor == "end":
            left = x - approx_w
            right = x
        else:
            left = x
            right = x + approx_w
        top = y - size * 0.9
        bottom = y + size * 0.25
        boxes.append((idx, content, left, top, right, bottom))

        if left < min_x + margin or right > max_x - margin:
            warnings.append(
                f"{path}: text #{idx} may exceed horizontal canvas bounds: {content[:100]!r}"
            )
        if y < min_y + margin or y > max_y - margin:
            warnings.append(
                f"{path}: text #{idx} may exceed vertical canvas bounds: {content[:100]!r}"
            )
        panel = assign_panel(panels, x, y)
        if panel is not None:
            panel_left, panel_top, panel_right, panel_bottom = panel
            panel_tolerance = 2.0
            if (
                left < panel_left - panel_tolerance
                or right > panel_right + panel_tolerance
                or top < panel_top - panel_tolerance
                or bottom > panel_bottom + panel_tolerance
            ):
                warnings.append(
                    f"{path}: text #{idx} may exceed panel bounds: {content[:100]!r}"
                )

    for i, box_a in enumerate(boxes):
        idx_a, text_a, left_a, top_a, right_a, bottom_a = box_a
        if len(text_a) <= 1:
            continue
        area_a = max(0.0, right_a - left_a) * max(0.0, bottom_a - top_a)
        for idx_b, text_b, left_b, top_b, right_b, bottom_b in boxes[i + 1 :]:
            if len(text_b) <= 1:
                continue
            overlap_w = min(right_a, right_b) - max(left_a, left_b)
            overlap_h = min(bottom_a, bottom_b) - max(top_a, top_b)
            if overlap_w <= 0 or overlap_h <= 0:
                continue
            area_b = max(0.0, right_b - left_b) * max(0.0, bottom_b - top_b)
            overlap_area = overlap_w * overlap_h
            if overlap_area > min(area_a, area_b) * 0.25:
                warnings.append(
                    f"{path}: possible text overlap between #{idx_a} and #{idx_b}: "
                    f"{text_a[:45]!r} / {text_b[:45]!r}"
                )

    rects = [node for node in root.iter() if local_name(node.tag) == "rect"]
    if len(rects) <= 1:
        warnings.append(f"{path}: few panel rectangles found; verify panel grid and whitespace manually")
    if not panels:
        warnings.append(f"{path}: no panel rectangles detected; panel-bound text overflow cannot be checked")

    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Smoke-check direct-text SVG figure layout.")
    parser.add_argument("svg", nargs="+", type=Path, help="SVG files to inspect")
    args = parser.parse_args()

    warnings: list[str] = []
    for path in args.svg:
        if not path.exists():
            warnings.append(f"{path}: file does not exist")
            continue
        warnings.extend(check_svg(path))

    for warning in warnings:
        print(f"WARNING: {warning}")

    return 1 if warnings else 0


if __name__ == "__main__":
    sys.exit(main())
