#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def call_blocks(text: str, token: str) -> list[tuple[int, str]]:
    blocks: list[tuple[int, str]] = []
    start = 0
    while True:
        index = text.find(token, start)
        if index == -1:
            break
        paren = text.find("(", index)
        if paren == -1:
            break
        depth = 0
        end = paren
        in_string: str | None = None
        escaped = False
        while end < len(text):
            char = text[end]
            if in_string:
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == in_string:
                    in_string = None
            else:
                if char in {"'", '"'}:
                    in_string = char
                elif char == "(":
                    depth += 1
                elif char == ")":
                    depth -= 1
                    if depth == 0:
                        end += 1
                        break
            end += 1
        blocks.append((index, text[index:end]))
        start = max(end, index + len(token))
    return blocks


def numeric_args(block: str) -> list[float]:
    after_paren = block.split("(", 1)[1] if "(" in block else block
    return [float(match.group(0)) for match in re.finditer(r"(?<![A-Za-z_])-?\d+(?:\.\d+)?", after_paren)]


def has_auto_aspect_parameter(text: str) -> bool:
    return bool(
        re.search(
            r"def\s+\w+\([^)]*aspect\s*:[^=,\)]*=\s*['\"]auto['\"]",
            text,
            flags=re.DOTALL,
        )
    )


def local_plot_context(text: str, index: int) -> str:
    start = text.rfind("plt.subplots", 0, index)
    if start == -1:
        start = max(0, index - 1500)
    return text[start:index]


def bottom_margin(context: str) -> float | None:
    matches = re.findall(r"subplots_adjust\([^)]*bottom\s*=\s*([0-9.]+)", context, flags=re.DOTALL)
    if not matches:
        return None
    return float(matches[-1])


def check_file(path: Path, *, footer_threshold: float) -> list[str]:
    text = path.read_text(encoding="utf-8")
    warnings: list[str] = []
    auto_aspect_parameter = has_auto_aspect_parameter(text)

    for index, block in call_blocks(text, "imshow"):
        normalized = re.sub(r"\s+", "", block)
        line = line_number(text, index)
        has_global_lonlat_extent = "extent=[-180,180,-90,90]" in normalized
        uses_auto_aspect = (
            "aspect=\"auto\"" in normalized
            or "aspect='auto'" in normalized
            or ("aspect=aspect" in normalized and auto_aspect_parameter)
        )
        if has_global_lonlat_extent and uses_auto_aspect:
            warnings.append(
                f"{path}:{line}: global lon-lat imshow uses aspect='auto'; preserve map/data aspect "
                "with equal/data aspect or an explicit projection-aware box_aspect"
            )
        uses_fixed_risk_scale = (
            ("vmin=1" in normalized and "vmax=5" in normalized)
            and ("RISK_CMAP" in block or "risk_green_yellow_red" in text or "green_yellow_red" in text)
        )
        if uses_fixed_risk_scale:
            warnings.append(
                f"{path}:{line}: fixed 1-5 green-yellow-red risk scale; verify the plotted data use the "
                "low/mid/high color range or choose a calibrated/sequential norm"
            )

    for index, block in call_blocks(text, "fig.text"):
        numbers = numeric_args(block)
        if len(numbers) < 2:
            continue
        y = numbers[1]
        context = local_plot_context(text, index)
        margin = bottom_margin(context)
        local_constrained = "constrained_layout=True" in context and "constrained_layout=False" not in context
        lacks_reserved_footer = margin is None or margin < y + 0.06
        if y <= 0.035 or (y <= footer_threshold and (local_constrained or lacks_reserved_footer)):
            warnings.append(
                f"{path}:{line_number(text, index)}: low fig.text y={y:g} without enough reserved footer space; "
                "reserve a footer row or increase bottom margin so notes cannot collide with x tick labels"
            )

    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Smoke-check plotting source for common figure-layout traps.")
    parser.add_argument("source", nargs="+", type=Path, help="Python plotting files to inspect")
    parser.add_argument("--footer-threshold", type=float, default=0.06, help="fig.text y position treated as footer-risk")
    args = parser.parse_args()

    warnings: list[str] = []
    for path in args.source:
        if not path.exists():
            warnings.append(f"{path}: file does not exist")
            continue
        if path.suffix.lower() != ".py":
            warnings.append(f"{path}: not a Python source file")
            continue
        warnings.extend(check_file(path, footer_threshold=args.footer_threshold))

    for warning in warnings:
        print(f"WARNING: {warning}")
    return 1 if warnings else 0


if __name__ == "__main__":
    sys.exit(main())
