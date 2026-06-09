#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path


FORMULA_RE = re.compile(r"(=|\b(sum|score|index|ratio|weight|threshold|sensitivity|class)\b)", re.I)


def read_docx_xml(path: Path) -> str:
    with zipfile.ZipFile(path) as archive:
        xml_parts = []
        for name in archive.namelist():
            if name.startswith("word/") and name.endswith(".xml"):
                xml_parts.append(archive.read(name).decode("utf-8", errors="ignore"))
    return "\n".join(xml_parts)


def strip_xml(xml: str) -> str:
    return re.sub(r"<[^>]+>", " ", xml)


def check_docx(path: Path) -> list[str]:
    if not path.exists():
        return [f"{path}: file does not exist"]
    if path.suffix.lower() != ".docx":
        return [f"{path}: not a .docx file"]

    try:
        xml = read_docx_xml(path)
    except (zipfile.BadZipFile, KeyError) as exc:
        return [f"{path}: cannot read DOCX: {exc}"]

    omath = len(re.findall(r"<m:oMath(?:\s|>)", xml))
    omath_para = len(re.findall(r"<m:oMathPara(?:\s|>)", xml))
    tables = len(re.findall(r"<w:tbl(?:\s|>)", xml))
    text = strip_xml(xml)
    formula_like_hits = len(FORMULA_RE.findall(text))
    warnings: list[str] = []

    print(
        f"{path}: oMath={omath} oMathPara={omath_para} tables={tables} "
        f"formula_like_hits={formula_like_hits}"
    )
    if formula_like_hits and omath == 0 and omath_para == 0:
        warnings.append(
            f"{path}: formula-like Methods/SI text found but no Word Office Math objects detected"
        )
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Smoke-check Word DOCX equation/table formatting.")
    parser.add_argument("docx", nargs="+", type=Path, help="DOCX files to inspect")
    args = parser.parse_args()

    warnings: list[str] = []
    for path in args.docx:
        warnings.extend(check_docx(path))

    for warning in warnings:
        print(f"WARNING: {warning}")
    return 1 if warnings else 0


if __name__ == "__main__":
    sys.exit(main())
