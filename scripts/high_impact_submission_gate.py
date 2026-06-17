#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path


REQUIRED_AUDITS = [
    "claim_figure_truth_table.tsv",
    "display_item_budget.tsv",
    "reviewer_panel_cards.md",
    "ncc_desk_rejection_memo.md",
    "score_caps.md",
    "abstract_claim_boundary.tsv",
    "figure_scientific_scores.tsv",
]

TRUTH_VERDICTS_BLOCKING_HIGH_SCORE = {
    "source_data_only",
    "ambiguous",
    "contradicted_by_figure",
    "unsupported",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_text(path: Path) -> str:
    if not path.exists():
        fail(f"missing required audit artifact: {path}")
    return path.read_text(encoding="utf-8")


def read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        fail(f"missing required audit artifact: {path}")
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    if not rows:
        fail(f"{path} must contain at least one data row")
    return rows


def norm(value: str | None) -> str:
    return (value or "").strip().lower()


def truthy(value: str | None) -> bool:
    return norm(value) in {"yes", "true", "1", "y", "central"}


def parse_int(value: str, *, context: str) -> int:
    match = re.search(r"\d+", value or "")
    if not match:
        fail(f"could not parse integer for {context}: {value!r}")
    return int(match.group(0))


def check_required_files(audit_dir: Path) -> None:
    missing = [name for name in REQUIRED_AUDITS if not (audit_dir / name).exists()]
    if missing:
        fail("missing required high-impact audit artifacts: " + ", ".join(missing))


def check_claim_truth_table(audit_dir: Path, reported_score: int) -> None:
    boundary_rows = read_tsv(audit_dir / "abstract_claim_boundary.tsv")
    truth_rows = read_tsv(audit_dir / "claim_figure_truth_table.tsv")

    truth_ids = {row.get("claim_id", "").strip() for row in truth_rows if row.get("claim_id")}
    abstract_ids = {
        row.get("claim_id", "").strip()
        for row in boundary_rows
        if row.get("claim_id") and ("abstract" in norm(row.get("location")) or not row.get("location"))
    }
    missing = sorted(abstract_ids - truth_ids)
    if missing:
        fail("abstract claims missing from claim_figure_truth_table.tsv: " + ", ".join(missing))

    for row in truth_rows:
        verdict = norm(row.get("verdict"))
        claim_id = row.get("claim_id", "<missing claim_id>")
        location = row.get("location", "")
        if verdict == "contradicted_by_figure":
            fail(f"claim {claim_id} is contradicted_by_figure at {location}")
        if reported_score >= 90 and "abstract" in norm(location) and verdict in TRUTH_VERDICTS_BLOCKING_HIGH_SCORE:
            fail(
                f"reported score {reported_score} requires visible proof for abstract claim "
                f"{claim_id}, but verdict is {verdict}"
            )


def check_figure_scores(audit_dir: Path) -> None:
    rows = read_tsv(audit_dir / "figure_scientific_scores.tsv")
    central_count = 0
    for row in rows:
        figure = row.get("figure", "<missing figure>")
        score = parse_int(row.get("scientific_score", ""), context=f"{figure} scientific_score")
        if score < 70:
            fail(f"{figure} scientific_score {score} is below the main-figure minimum 70")
        if truthy(row.get("central_figure")):
            central_count += 1
            if score < 80:
                fail(f"{figure} is central but scientific_score {score} is below 80")
    if central_count == 0:
        fail("figure_scientific_scores.tsv must mark at least one central_figure")


def parse_score_caps(text: str) -> tuple[list[tuple[str, int]], int | None]:
    major_match = re.search(r"(?im)^\s*major_issue_count\s*:\s*(\d+)\s*$", text)
    major_issue_count = int(major_match.group(1)) if major_match else None

    active_caps: list[tuple[str, int]] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line.startswith("|") or "---" in line:
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < 3:
            continue
        if cells[0].lower() == "cap":
            continue
        applies = norm(cells[1])
        if applies not in {"yes", "true", "y", "applies"}:
            continue
        cap_value = parse_int(cells[2], context=f"active cap {cells[0]}")
        active_caps.append((cells[0], cap_value))
    return active_caps, major_issue_count


def check_score_caps(audit_dir: Path, reported_score: int) -> None:
    text = load_text(audit_dir / "score_caps.md")
    active_caps, major_issue_count = parse_score_caps(text)
    for cap_name, cap_value in active_caps:
        if cap_value < reported_score:
            fail(f"active cap `{cap_name}` ({cap_value}) is below reported score {reported_score}")

    if reported_score >= 90:
        if major_issue_count is None:
            fail("score_caps.md must state major_issue_count before reporting score >=90")
        if major_issue_count != 0:
            fail(f"reported score >=90 requires major_issue_count == 0, got {major_issue_count}")


def check_content_type_decision(audit_dir: Path) -> None:
    text = load_text(audit_dir / "ncc_desk_rejection_memo.md")
    required = ["Content-type identity verdict:", "Article vs Analysis decision:"]
    missing = [term for term in required if term not in text]
    if missing:
        fail("ncc_desk_rejection_memo.md is missing: " + ", ".join(missing))


def check_reviewer_panel(audit_dir: Path) -> None:
    text = load_text(audit_dir / "reviewer_panel_cards.md")
    headings = re.findall(r"(?m)^##\s+(.+?)\s*$", text)
    if len(headings) < 5:
        fail("reviewer_panel_cards.md must include at least four specialist reviewers plus one figure editor")
    if not any("figure editor" in heading.lower() for heading in headings):
        fail("reviewer_panel_cards.md must include a figure editor")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate high-impact journal adversarial audit artifacts before submission-ready claims."
    )
    parser.add_argument("package_root", nargs="?", default=".", help="Project or package root containing audits/")
    parser.add_argument("--reported-score", type=int, required=True, help="Score the workflow plans to report")
    args = parser.parse_args()

    root = Path(args.package_root).expanduser().resolve()
    audit_dir = root / "audits"
    if not audit_dir.is_dir():
        fail(f"missing audits directory: {audit_dir}")

    check_required_files(audit_dir)
    check_claim_truth_table(audit_dir, args.reported_score)
    check_figure_scores(audit_dir)
    check_score_caps(audit_dir, args.reported_score)
    check_content_type_decision(audit_dir)
    check_reviewer_panel(audit_dir)

    print(f"OK: high-impact submission gate passed for {root}")


if __name__ == "__main__":
    main()
