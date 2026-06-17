from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GATE = ROOT / "scripts" / "high_impact_submission_gate.py"


def write_minimal_audit(root: Path, *, claim_verdict: str = "proven_visibly", active_cap: int = 95, major_issue_count: int = 0) -> None:
    audits = root / "audits"
    audits.mkdir()

    (audits / "abstract_claim_boundary.tsv").write_text(
        "claim_id\tlocation\tmetric\tallowed_wording\tforbidden_wording\n"
        "C1\tAbstract\tordinal diagnostic rank\tranks higher under the diagnostic index\tis physically more stable\n",
        encoding="utf-8",
    )
    (audits / "claim_figure_truth_table.tsv").write_text(
        "claim_id\texact claim\tlocation\trequired figure panel\tobserved visual evidence\t"
        "source-data file/column\teffect size\tn/denominator\tuncertainty\tallowed wording\tforbidden wording\tverdict\n"
        f"C1\tOpen ocean ranks higher under the index\tAbstract\tFig. 4a\tVisible rank-one probability\t"
        f"source.tsv/rank_one\t0.42\t10/10\t95% CI\tordinal rank\tphysical stability\t{claim_verdict}\n",
        encoding="utf-8",
    )
    (audits / "display_item_budget.tsv").write_text(
        "Figure\tOne-sentence job\tAbstract claim supported\tUnique result?\tEffect size visible?\t"
        "Uncertainty visible?\tSource data\tKeep main?\tRedesign action\n"
        "Figure 4\tTest central ordering\tC1\tYes\tYes\tYes\tsource.tsv\tYes\tNone\n",
        encoding="utf-8",
    )
    (audits / "figure_scientific_scores.tsv").write_text(
        "figure\tscientific_score\tcentral_figure\n"
        "Figure 4\t85\tYes\n",
        encoding="utf-8",
    )
    (audits / "reviewer_panel_cards.md").write_text(
        "# Reviewer Panel Cards\n\n"
        "## carbon-cycle / global carbon budget\n"
        "- Severity: minor\n\n"
        "## terrestrial carbon and disturbance\n"
        "- Severity: minor\n\n"
        "## ocean carbon / marine biogeochemistry\n"
        "- Severity: minor\n\n"
        "## quantitative methods / uncertainty\n"
        "- Severity: minor\n\n"
        "## figure editor\n"
        "- Severity: minor\n",
        encoding="utf-8",
    )
    (audits / "ncc_desk_rejection_memo.md").write_text(
        "# NCC Desk-Rejection Memo\n\n"
        "Content-type identity verdict: Article\n"
        "Article vs Analysis decision: Article identity supported by inspected figure-visible evidence.\n",
        encoding="utf-8",
    )
    (audits / "score_caps.md").write_text(
        "# Score Caps\n\n"
        f"major_issue_count: {major_issue_count}\n\n"
        "| Cap | Applies | Cap value | Why |\n"
        "|---|---|---:|---|\n"
        f"| Main-figure ambiguity | Yes | {active_cap} | active cap for test |\n",
        encoding="utf-8",
    )


def run_gate(package_root: Path, reported_score: int) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(GATE), str(package_root), "--reported-score", str(reported_score)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


class HighImpactSubmissionGateTests(unittest.TestCase):
    def test_gate_fails_when_abstract_claim_is_contradicted_by_figure(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            package_root = Path(tmp)
            write_minimal_audit(package_root, claim_verdict="contradicted_by_figure")

            result = run_gate(package_root, reported_score=95)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("contradicted_by_figure", result.stderr)

    def test_gate_fails_when_reported_score_exceeds_active_cap(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            package_root = Path(tmp)
            write_minimal_audit(package_root, active_cap=70)

            result = run_gate(package_root, reported_score=90)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("active cap", result.stderr)

    def test_gate_passes_for_complete_high_impact_audit(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            package_root = Path(tmp)
            write_minimal_audit(package_root)

            result = run_gate(package_root, reported_score=92)

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("OK:", result.stdout)


if __name__ == "__main__":
    unittest.main()
