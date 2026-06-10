#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


def sniff_dialect(path: Path) -> csv.Dialect:
    sample = path.read_text(encoding="utf-8")[:4096]
    if "\t" in sample:
        return csv.excel_tab
    try:
        return csv.Sniffer().sniff(sample)
    except csv.Error:
        return csv.excel


def values_from_file(path: Path, column: str) -> list[float]:
    dialect = sniff_dialect(path)
    values: list[float] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, dialect=dialect)
        if reader.fieldnames is None:
            raise ValueError("missing header row")
        if column not in reader.fieldnames:
            raise ValueError(f"missing column {column!r}")
        for row in reader:
            raw = (row.get(column) or "").strip()
            if not raw or raw == column:
                continue
            try:
                values.append(float(raw))
            except ValueError:
                continue
    return values


def main() -> int:
    parser = argparse.ArgumentParser(description="Smoke-check whether figure data meaningfully use a color scale.")
    parser.add_argument("table", nargs="+", type=Path, help="CSV/TSV source-data tables")
    parser.add_argument("--column", required=True, help="Numeric column plotted as color")
    parser.add_argument("--vmin", type=float, required=True, help="Color scale lower bound")
    parser.add_argument("--vmax", type=float, required=True, help="Color scale upper bound")
    parser.add_argument(
        "--min-range-fraction",
        type=float,
        default=0.25,
        help="warn when observed range uses less than this fraction of the color scale",
    )
    parser.add_argument(
        "--unused-side-fraction",
        type=float,
        default=0.35,
        help="warn when one side of the color scale is mostly unused",
    )
    args = parser.parse_args()

    values: list[float] = []
    warnings: list[str] = []
    for path in args.table:
        if not path.exists():
            warnings.append(f"{path}: file does not exist")
            continue
        try:
            values.extend(values_from_file(path, args.column))
        except (OSError, ValueError, csv.Error) as exc:
            warnings.append(f"{path}: cannot read scale data: {exc}")

    if not values:
        warnings.append(f"no numeric values found for column {args.column!r}")
    else:
        observed_min = min(values)
        observed_max = max(values)
        scale_span = args.vmax - args.vmin
        if scale_span <= 0:
            warnings.append("vmax must be greater than vmin")
        else:
            used_fraction = (observed_max - observed_min) / scale_span
            unused_low = (observed_min - args.vmin) / scale_span
            unused_high = (args.vmax - observed_max) / scale_span
            print(
                f"{args.column}: n={len(values)} observed={observed_min:.3g}-{observed_max:.3g} "
                f"scale={args.vmin:.3g}-{args.vmax:.3g} used={used_fraction:.1%} "
                f"unused_low={unused_low:.1%} unused_high={unused_high:.1%}"
            )
            if used_fraction < args.min_range_fraction:
                warnings.append(
                    f"{args.column}: observed values use only {used_fraction:.1%} of the color scale; "
                    "use a calibrated norm, annotate observed range, or choose a sequential palette"
                )
            if unused_low > args.unused_side_fraction:
                warnings.append(
                    f"{args.column}: lower {unused_low:.1%} of the color scale is unused; "
                    "low-color semantics such as green may be misleading"
                )
            if unused_high > args.unused_side_fraction:
                warnings.append(
                    f"{args.column}: upper {unused_high:.1%} of the color scale is unused; "
                    "high-color semantics may be misleading"
                )

    for warning in warnings:
        print(f"WARNING: {warning}")
    return 1 if warnings else 0


if __name__ == "__main__":
    sys.exit(main())
