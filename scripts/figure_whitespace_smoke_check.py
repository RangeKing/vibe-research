#!/usr/bin/env python3

from __future__ import annotations

import argparse
import collections
import struct
import sys
import zlib
from pathlib import Path


PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


class PngDecodeError(ValueError):
    pass


def paeth(a: int, b: int, c: int) -> int:
    p = a + b - c
    pa = abs(p - a)
    pb = abs(p - b)
    pc = abs(p - c)
    if pa <= pb and pa <= pc:
        return a
    if pb <= pc:
        return b
    return c


def parse_png(path: Path) -> tuple[int, int, int, list[bytes], list[tuple[int, int, int]], bytes]:
    data = path.read_bytes()
    if not data.startswith(PNG_SIGNATURE):
        raise PngDecodeError("not a PNG file")

    offset = len(PNG_SIGNATURE)
    width = height = bit_depth = color_type = None
    palette: list[tuple[int, int, int]] = []
    transparency = b""
    idat_parts: list[bytes] = []

    while offset + 8 <= len(data):
        length = struct.unpack(">I", data[offset : offset + 4])[0]
        chunk_type = data[offset + 4 : offset + 8]
        chunk_data = data[offset + 8 : offset + 8 + length]
        offset += 12 + length

        if chunk_type == b"IHDR":
            width, height, bit_depth, color_type, compression, filter_method, interlace = struct.unpack(
                ">IIBBBBB", chunk_data
            )
            if compression != 0 or filter_method != 0 or interlace != 0:
                raise PngDecodeError("unsupported PNG compression/filter/interlace mode")
        elif chunk_type == b"PLTE":
            palette = [
                tuple(chunk_data[i : i + 3])  # type: ignore[arg-type]
                for i in range(0, len(chunk_data), 3)
                if i + 2 < len(chunk_data)
            ]
        elif chunk_type == b"tRNS":
            transparency = chunk_data
        elif chunk_type == b"IDAT":
            idat_parts.append(chunk_data)
        elif chunk_type == b"IEND":
            break

    if width is None or height is None or bit_depth is None or color_type is None:
        raise PngDecodeError("missing IHDR")
    if bit_depth != 8:
        raise PngDecodeError(f"unsupported PNG bit depth {bit_depth}; only 8-bit PNG is supported")
    if color_type not in {0, 2, 3, 4, 6}:
        raise PngDecodeError(f"unsupported PNG color type {color_type}")

    channels_by_type = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}
    channels = channels_by_type[color_type]
    row_bytes = width * channels
    raw = zlib.decompress(b"".join(idat_parts))
    expected = height * (row_bytes + 1)
    if len(raw) < expected:
        raise PngDecodeError("truncated IDAT stream")

    rows: list[bytes] = []
    previous = bytearray(row_bytes)
    pos = 0
    for _ in range(height):
        filter_type = raw[pos]
        pos += 1
        current = bytearray(raw[pos : pos + row_bytes])
        pos += row_bytes
        bpp = channels

        if filter_type == 1:
            for i in range(row_bytes):
                left = current[i - bpp] if i >= bpp else 0
                current[i] = (current[i] + left) & 0xFF
        elif filter_type == 2:
            for i in range(row_bytes):
                current[i] = (current[i] + previous[i]) & 0xFF
        elif filter_type == 3:
            for i in range(row_bytes):
                left = current[i - bpp] if i >= bpp else 0
                current[i] = (current[i] + ((left + previous[i]) // 2)) & 0xFF
        elif filter_type == 4:
            for i in range(row_bytes):
                left = current[i - bpp] if i >= bpp else 0
                up = previous[i]
                upper_left = previous[i - bpp] if i >= bpp else 0
                current[i] = (current[i] + paeth(left, up, upper_left)) & 0xFF
        elif filter_type != 0:
            raise PngDecodeError(f"unsupported PNG filter type {filter_type}")

        rows.append(bytes(current))
        previous = current

    return width, height, color_type, rows, palette, transparency


def pixel_rgba(
    row: bytes,
    x: int,
    color_type: int,
    palette: list[tuple[int, int, int]],
    transparency: bytes,
) -> tuple[int, int, int, int]:
    if color_type == 0:
        value = row[x]
        alpha = 0 if len(transparency) >= 2 and value == transparency[1] else 255
        return value, value, value, alpha
    if color_type == 2:
        pos = x * 3
        r, g, b = row[pos : pos + 3]
        return r, g, b, 255
    if color_type == 3:
        index = row[x]
        r, g, b = palette[index] if index < len(palette) else (0, 0, 0)
        alpha = transparency[index] if index < len(transparency) else 255
        return r, g, b, alpha
    if color_type == 4:
        pos = x * 2
        value, alpha = row[pos : pos + 2]
        return value, value, value, alpha
    pos = x * 4
    r, g, b, alpha = row[pos : pos + 4]
    return r, g, b, alpha


def quantize_rgb(pixel: tuple[int, int, int, int]) -> tuple[int, int, int]:
    r, g, b, _ = pixel
    return (
        min(255, round(r / 8) * 8),
        min(255, round(g / 8) * 8),
        min(255, round(b / 8) * 8),
    )


def background_color(
    width: int,
    height: int,
    color_type: int,
    rows: list[bytes],
    palette: list[tuple[int, int, int]],
    transparency: bytes,
) -> tuple[int, int, int]:
    samples: list[tuple[int, int, int]] = []
    for x in range(width):
        samples.append(quantize_rgb(pixel_rgba(rows[0], x, color_type, palette, transparency)))
        samples.append(quantize_rgb(pixel_rgba(rows[-1], x, color_type, palette, transparency)))
    for y in range(height):
        samples.append(quantize_rgb(pixel_rgba(rows[y], 0, color_type, palette, transparency)))
        samples.append(quantize_rgb(pixel_rgba(rows[y], width - 1, color_type, palette, transparency)))
    return collections.Counter(samples).most_common(1)[0][0]


def is_content(pixel: tuple[int, int, int, int], bg: tuple[int, int, int], threshold: int) -> bool:
    r, g, b, alpha = pixel
    if alpha < 16:
        return False
    return abs(r - bg[0]) + abs(g - bg[1]) + abs(b - bg[2]) > threshold


def check_png(path: Path, *, side_threshold: float, imbalance_threshold: float, color_threshold: int) -> list[str]:
    width, height, color_type, rows, palette, transparency = parse_png(path)
    bg = background_color(width, height, color_type, rows, palette, transparency)

    left = width
    right = -1
    top = height
    bottom = -1
    content_pixels = 0

    for y, row in enumerate(rows):
        for x in range(width):
            if not is_content(pixel_rgba(row, x, color_type, palette, transparency), bg, color_threshold):
                continue
            content_pixels += 1
            left = min(left, x)
            right = max(right, x)
            top = min(top, y)
            bottom = max(bottom, y)

    if right < left or bottom < top:
        return [f"{path}: no non-background content detected"]

    left_margin = left / width
    right_margin = (width - 1 - right) / width
    top_margin = top / height
    bottom_margin = (height - 1 - bottom) / height
    content_width = (right - left + 1) / width
    content_height = (bottom - top + 1) / height
    content_area = content_pixels / (width * height)

    print(
        f"{path}: content_bbox=({left},{top})-({right},{bottom}) "
        f"margins=L{left_margin:.1%},R{right_margin:.1%},T{top_margin:.1%},B{bottom_margin:.1%} "
        f"content_width={content_width:.1%} content_height={content_height:.1%} "
        f"content_pixel_area={content_area:.1%} background_rgb={bg}"
    )

    warnings: list[str] = []
    side_margins = {
        "left": left_margin,
        "right": right_margin,
        "top": top_margin,
        "bottom": bottom_margin,
    }
    opposites = {"left": right_margin, "right": left_margin, "top": bottom_margin, "bottom": top_margin}
    for side, margin in side_margins.items():
        if margin >= side_threshold and margin - opposites[side] >= imbalance_threshold:
            warnings.append(
                f"{path}: large {side} whitespace margin ({margin:.1%}) relative to opposite side "
                f"({opposites[side]:.1%}); inspect rendered figure balance"
            )

    if content_width < 0.58:
        warnings.append(f"{path}: content occupies only {content_width:.1%} of canvas width")
    if content_height < 0.58:
        warnings.append(f"{path}: content occupies only {content_height:.1%} of canvas height")

    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Smoke-check raster figure whitespace and canvas balance.")
    parser.add_argument("image", nargs="+", type=Path, help="PNG figure files to inspect")
    parser.add_argument("--side-threshold", type=float, default=0.22, help="margin ratio that triggers review")
    parser.add_argument(
        "--imbalance-threshold",
        type=float,
        default=0.10,
        help="minimum side-vs-opposite margin gap that triggers review",
    )
    parser.add_argument("--color-threshold", type=int, default=36, help="RGB distance from background counted as content")
    args = parser.parse_args()

    warnings: list[str] = []
    for path in args.image:
        if not path.exists():
            warnings.append(f"{path}: file does not exist")
            continue
        if path.suffix.lower() != ".png":
            warnings.append(f"{path}: unsupported raster format; export/check a PNG preview")
            continue
        try:
            warnings.extend(
                check_png(
                    path,
                    side_threshold=args.side_threshold,
                    imbalance_threshold=args.imbalance_threshold,
                    color_threshold=args.color_threshold,
                )
            )
        except (OSError, PngDecodeError, zlib.error, struct.error) as exc:
            warnings.append(f"{path}: cannot inspect PNG layout: {exc}")

    for warning in warnings:
        print(f"WARNING: {warning}")
    return 1 if warnings else 0


if __name__ == "__main__":
    sys.exit(main())
