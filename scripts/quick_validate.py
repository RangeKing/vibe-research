#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path


EXPECTED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "system/coordinator.md",
    "system/routing.md",
    "system/guardrails.md",
    "references/high-journal-expression.md",
    "references/reference-adequacy-audit.md",
    "references/target-journal-scorecard.md",
    "references/sentence-level-writing-audit.md",
    "templates/research_task_packet.md",
    "templates/target_journal_scorecard.md",
    "templates/reference_coverage_map.md",
    "templates/campaign_checkpoint.md",
    "templates/research_memory.md",
    "templates/polish_pass.md",
    "templates/writing_quality_review.md",
    "scripts/svg_layout_smoke_check.py",
    "scripts/docx_equation_smoke_check.py",
    "scripts/figure_whitespace_smoke_check.py",
    "scripts/figure_code_smoke_check.py",
    "scripts/figure_scale_smoke_check.py",
]


SOURCE_ONLY_DOCS = [
    "README.md",
    "README_CN.md",
    "platforms/codex/README.md",
    "platforms/claude-code/README.md",
    "platforms/openclaw/README.md",
]

RESOURCE_PATH_RE = re.compile(
    r"`((?:agents|platforms|references|roles|scripts|system|templates)/[^`]+)`"
)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_text(path: Path) -> str:
    if not path.exists():
        fail(f"missing required file: {path}")
    return path.read_text(encoding="utf-8")


def parse_frontmatter(skill_path: Path) -> dict:
    text = load_text(skill_path)
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        fail(f"{skill_path} is missing YAML frontmatter")
    data = parse_simple_yaml_map(match.group(1), context=f"{skill_path} frontmatter")
    if not isinstance(data, dict):
        fail(f"{skill_path} frontmatter must be a mapping")
    return data


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def parse_simple_yaml_map(text: str, *, context: str) -> dict:
    result: dict[str, object] = {}
    stack: list[tuple[int, dict[str, object]]] = [(-1, result)]

    for lineno, raw_line in enumerate(text.splitlines(), start=1):
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        indent = len(raw_line) - len(raw_line.lstrip(" "))
        line = raw_line.strip()
        if ":" not in line:
            fail(f"{context} has unsupported YAML syntax on line {lineno}: {raw_line}")

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()

        while len(stack) > 1 and indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]

        if not value:
            child: dict[str, object] = {}
            parent[key] = child
            stack.append((indent, child))
            continue

        parent[key] = strip_quotes(value)

    return result


def validate_skill_md(root: Path) -> None:
    data = parse_frontmatter(root / "SKILL.md")
    if list(data.keys()) != ["name", "description"]:
        fail("SKILL.md frontmatter must contain only `name` and `description` in that order")

    name = data["name"]
    description = data["description"]
    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9-]{1,64}", name):
        fail("SKILL.md `name` must match ^[a-z0-9-]{1,64}$")
    if name != root.name:
        fail(f"SKILL.md name `{name}` does not match folder name `{root.name}`")
    if not isinstance(description, str) or not description.strip():
        fail("SKILL.md `description` must be a non-empty string")
    if not description.startswith("Use when "):
        fail("SKILL.md `description` must start with `Use when ` per skill-creator guidance")
    if len(description) > 500:
        fail("SKILL.md `description` should stay at or below 500 characters")


def validate_openai_yaml(root: Path) -> None:
    path = root / "agents/openai.yaml"
    data = parse_simple_yaml_map(load_text(path), context=str(path))
    if not isinstance(data, dict):
        fail("agents/openai.yaml must be a mapping")

    interface = data.get("interface")
    if not isinstance(interface, dict):
        fail("agents/openai.yaml must contain an `interface` mapping")

    required = ["display_name", "short_description", "default_prompt"]
    missing = [key for key in required if not isinstance(interface.get(key), str) or not interface[key].strip()]
    if missing:
        fail(f"agents/openai.yaml is missing non-empty interface fields: {', '.join(missing)}")

    short_description = interface["short_description"]
    if not 25 <= len(short_description) <= 64:
        fail("agents/openai.yaml interface.short_description must be 25-64 characters")

    default_prompt = interface["default_prompt"]
    skill_name = parse_frontmatter(root / "SKILL.md")["name"]
    if f"${skill_name}" not in default_prompt:
        fail(f"agents/openai.yaml interface.default_prompt must mention `${skill_name}`")


def validate_required_files(root: Path) -> None:
    missing = [rel for rel in EXPECTED_FILES if not (root / rel).exists()]
    if missing:
        fail(f"missing required repository files: {', '.join(missing)}")


def validate_referenced_paths(root: Path) -> None:
    skill_text = load_text(root / "SKILL.md")
    missing: list[str] = []
    for match in RESOURCE_PATH_RE.finditer(skill_text):
        rel = match.group(1)
        if not (root / rel).exists():
            missing.append(rel)
    if missing:
        fail(f"SKILL.md references missing resource paths: {', '.join(sorted(set(missing)))}")


def validate_long_markdown_navigation(root: Path) -> None:
    missing: list[str] = []
    for base in ["references", "system"]:
        for path in (root / base).glob("*.md"):
            text = load_text(path)
            if len(text.splitlines()) > 100 and "## Navigation" not in text[:1000]:
                missing.append(str(path.relative_to(root)))
    if missing:
        fail(f"long reference/system files need early `## Navigation` sections: {', '.join(missing)}")


def validate_source_packaging_note(root: Path) -> None:
    existing = [rel for rel in SOURCE_ONLY_DOCS if (root / rel).exists()]
    if not existing:
        return

    skill_text = load_text(root / "SKILL.md")
    if "runtime installation/export should omit source-only documentation" not in skill_text:
        fail("source README files are allowed, but SKILL.md must document that runtime installs omit source-only docs")

    print("NOTE: README/platform docs are source-only; runtime install/export should omit them.")


def validate_managed_harness_surface(root: Path) -> None:
    skill_text = load_text(root / "SKILL.md")
    required_terms = [
        "doctor",
        "packetize",
        "execute",
        "verify",
        "distill",
        "checkpoint",
        "wake",
        "merge",
        "reference-adequacy",
    ]
    missing = [term for term in required_terms if term not in skill_text]
    if missing:
        fail(f"SKILL.md is missing managed-harness or Chinese-entry terms: {', '.join(missing)}")

    chinese_triggers = [
        "评估这篇稿子",
        "继续这个项目",
        "重写摘要",
        "回复审稿意见",
    ]
    if not any(term in skill_text for term in chinese_triggers):
        fail("SKILL.md is missing Chinese trigger phrases")

    if skill_text.count("- failure risks such as") != 1:
        fail("SKILL.md must contain one consolidated `failure risks such as` bullet")

    packet_text = load_text(root / "templates/research_task_packet.md")
    for field in ["session_state", "frontier", "inputs", "recovery_mode", "merge_target", "stop_conditions", "reference_state", "citation_plan"]:
        if field not in packet_text:
            fail(f"templates/research_task_packet.md is missing `{field}`")

    coverage_text = load_text(root / "templates/reference_coverage_map.md")
    for field in ["Reference state", "Claim buckets", "Priority insertion plan", "Sequence and formatting checks", "Stop condition before polish"]:
        if field not in coverage_text:
            fail(f"templates/reference_coverage_map.md is missing `{field}`")

    checkpoint_text = load_text(root / "templates/campaign_checkpoint.md")
    for field in ["Last trustworthy state", "Active frontier", "Open loops", "Blocked on", "Next wake instruction"]:
        if field not in checkpoint_text:
            fail(f"templates/campaign_checkpoint.md is missing `{field}`")

    memory_text = load_text(root / "templates/research_memory.md")
    for field in ["Reusable heuristics", "Decision rules", "Killed patterns", "Do not repeat"]:
        if field not in memory_text:
            fail(f"templates/research_memory.md is missing `{field}`")


def validate_parameter_provenance_surface(root: Path) -> None:
    required_terms = {
        "SKILL.md": [
            "parameter provenance",
            "parameter_guessing",
            "parameter_provenance_gap",
        ],
        "system/guardrails.md": [
            "parameters, coefficients, thresholds, conversion factors, priors, scenario assumptions",
        ],
        "references/reference-adequacy-audit.md": [
            "Parameter provenance",
            "Do not use self-estimated values",
        ],
        "roles/assess.md": [
            "parameter provenance",
        ],
        "roles/claim.md": [
            "parameter provenance",
        ],
        "roles/draft.md": [
            "parameter provenance",
        ],
        "templates/claims_evidence_map.md": [
            "parameter_provenance",
        ],
        "templates/reference_coverage_map.md": [
            "Parameter and assumption support",
        ],
        "templates/evidence_register.md": [
            "Parameter / assumption",
        ],
    }

    for rel, terms in required_terms.items():
        text = load_text(root / rel)
        missing = [term for term in terms if term not in text]
        if missing:
            fail(f"{rel} is missing parameter provenance terms: {', '.join(missing)}")


def validate_target_journal_scorecard_surface(root: Path) -> None:
    required_terms = {
        "SKILL.md": [
            "target-journal scorecard",
            "Codex Goal context",
            "journal_score_gap",
            "Methods/SI reproducibility gate",
        ],
        "system/coordinator.md": [
            "Codex Goal context",
            "target-journal scorecard",
            "Do not create a separate internal goal mode",
        ],
        "system/routing.md": [
            "scorecard",
            "journal_score_gap",
            "Codex Goal",
        ],
        "roles/assess.md": [
            "target-journal scorecard",
        ],
        "roles/journal.md": [
            "target-journal scorecard",
        ],
        "references/target-journal-scorecard.md": [
            "This score is not an acceptance probability",
            "Blocking caps",
            "Codex Goal compatibility",
            "Artifact update policy",
            "target_journal_scorecard.md",
            "Figure quality and visual communication",
            "High-score gates",
            "Methods and SI are too thin",
        ],
        "templates/target_journal_scorecard.md": [
            "Artifact update",
            "Overall score",
            "Score history",
            "Gap to target",
            "Blocking caps",
            "Figure readability or production-layout failure",
            "Codex Goal next actions",
            "Methods/SI reproducibility gate",
            "Word equation objects missing",
        ],
        "templates/research_task_packet.md": [
            "codex_goal_context",
            "scorecard_plan",
        ],
        "templates/journal_fit_report.md": [
            "Target-journal scorecard",
        ],
        "templates/research_assessment.md": [
            "Target-journal scorecard",
        ],
    }

    for rel, terms in required_terms.items():
        text = load_text(root / rel)
        missing = [term for term in terms if term not in text]
        if missing:
            fail(f"{rel} is missing target-journal scorecard terms: {', '.join(missing)}")

    forbidden_terms = [
        "goal_mode",
        "goal-mode",
        "Goal mode is active",
        "In Goal mode",
        "Goal-mode loop",
        "Goal-mode next actions",
    ]
    forbidden_hits: list[str] = []
    for rel in [
        "SKILL.md",
        "agents/openai.yaml",
        "system/coordinator.md",
        "system/routing.md",
        "roles/assess.md",
        "roles/journal.md",
        "roles/draft.md",
        "roles/polish.md",
        "roles/revise.md",
        "references/target-journal-scorecard.md",
        "templates/target_journal_scorecard.md",
        "templates/research_task_packet.md",
    ]:
        text = load_text(root / rel)
        for term in forbidden_terms:
            if term in text:
                forbidden_hits.append(f"{rel}: {term}")
    if forbidden_hits:
        fail("target-journal scorecard must not define an internal goal mode: " + "; ".join(forbidden_hits))


def validate_score_calibration_surface(root: Path) -> None:
    """Check that the strict score-band calibration is present and consistent everywhere."""
    band_tokens = ["0-59", "60-69", "70-79", "80-89", "90-99"]

    required_terms = {
        "references/target-journal-scorecard.md": [
            "## Score bands and calibration",
            "## Conservative scoring defaults",
            "## Anti-inflation guardrails",
            "## Calibration anchors",
            "Not submission-ready",
            "Barely submission-ready",
            "Fluent writing alone never raises the score",
            "Any fatal flaw caps the total below 60",
            "Any major unresolved flaw caps the total below 80",
            "Strong sections do not compensate for fatal flaws",
            "must not score above 60",
            "must not score above 70",
            "must not score above 80",
            "must not score above 90",
            "95+ is possible only",
            "100 is effectively reserved",
            "report the lower one",
            "Blockers to the next band",
            "Path to higher bands",
            "Main reasons for the score",
            "Score band meaning",
        ],
        "templates/target_journal_scorecard.md": [
            "Score band meaning",
            "Main reasons for the score",
            "Anti-inflation check",
            "Blockers to the next band",
            "Path to higher bands",
            "To reach 60",
            "To reach 70",
            "To reach 80",
            "To reach 90",
            "To reach 100",
        ],
        "SKILL.md": [
            "0-59 not submission-ready",
            "90-99 very strong and rare",
            "fatal flaw caps the total below 60",
            "major unresolved flaw caps it below 80",
            "blockers to the next band",
        ],
        "roles/assess.md": [
            "strict band calibration",
            "anti-inflation guardrails",
            "blockers preventing the next band",
        ],
        "roles/journal.md": [
            "strict band calibration",
            "blockers to the next band",
        ],
        "system/coordinator.md": [
            "0-59 not submission-ready",
            "uncertain scores round down",
        ],
        "system/routing.md": [
            "strict band calibration",
            "fatal flaws cap below 60",
        ],
    }

    for rel, terms in required_terms.items():
        text = load_text(root / rel)
        missing = [term for term in terms if term not in text]
        if missing:
            fail(f"{rel} is missing strict score-calibration terms: {', '.join(missing)}")

    for rel in ["references/target-journal-scorecard.md", "templates/target_journal_scorecard.md"]:
        text = load_text(root / rel)
        missing_bands = [band for band in band_tokens if band not in text]
        if missing_bands:
            fail(f"{rel} is missing score-band tokens: {', '.join(missing_bands)}")

    # Cap values in the template must respect band semantics:
    # fatal < 60, major < 80, package-level < 90.
    severity_limits = {"Fatal": 60, "Major": 80, "Package": 90}
    template_text = load_text(root / "templates/target_journal_scorecard.md")
    cap_rows = 0
    for line in template_text.splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and cells[1] in severity_limits and cells[2].isdigit():
            cap_rows += 1
            cap_value = int(cells[2])
            limit = severity_limits[cells[1]]
            if cap_value >= limit:
                fail(
                    f"templates/target_journal_scorecard.md cap `{cells[0]}` has severity "
                    f"{cells[1]} but cap value {cap_value} >= {limit}"
                )
    if cap_rows < 10:
        fail(
            "templates/target_journal_scorecard.md blocking-caps table must classify caps as "
            f"Fatal/Major/Package with numeric cap values, found only {cap_rows} classified rows"
        )

    # Lenient scoring language must never come back.
    forbidden_terms = [
        "score generously",
        "be generous with the score",
        "round the score up",
        "default to a high score",
        "90 = good",
        "95 = excellent",
        "99 = almost ready",
        "almost ready to submit, score",
        "reward fluent writing",
    ]
    forbidden_hits: list[str] = []
    for path in sorted(root.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = load_text(path)
        for term in forbidden_terms:
            if term in text:
                forbidden_hits.append(f"{path.relative_to(root)}: {term}")
    if forbidden_hits:
        fail("inflated-scoring language found: " + "; ".join(forbidden_hits))


def validate_target_journal_scorecard_points(root: Path) -> None:
    for rel in ["references/target-journal-scorecard.md", "templates/target_journal_scorecard.md"]:
        text = load_text(root / rel)
        points: list[int] = []
        in_dimension_table = False
        for line in text.splitlines():
            if line.startswith("| Axis | Points |") or line.startswith("| Dimension | Max |"):
                in_dimension_table = True
                continue
            if in_dimension_table and not line.startswith("|"):
                break
            if not in_dimension_table:
                continue
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) < 2 or cells[1] in {"Points", "Max", "---:"}:
                continue
            if cells[1].isdigit():
                points.append(int(cells[1]))
        if sum(points) != 100:
            fail(f"{rel} scorecard dimension points must sum to 100, got {sum(points)}")


def validate_figure_layout_surface(root: Path) -> None:
    required_terms = {
        "SKILL.md": [
            "production-layout",
            "text wrapping",
            "rendered PNG/SVG whitespace balance",
            "map aspect",
            "color-scale/data-range fit",
            "footer collision",
            "rendered legibility",
        ],
        "references/figure-storytelling.md": [
            "Production layout contract",
            "hard text boundary",
            "wrap_text",
            "scripts/svg_layout_smoke_check.py",
            "scripts/figure_whitespace_smoke_check.py",
            "scripts/figure_code_smoke_check.py",
            "scripts/figure_scale_smoke_check.py",
            "Render the final figure",
            "content bounding-box imbalance",
            "--check-bottom-text",
            "Geospatial Panels And Color Scales",
            "aspect=\"auto\"",
            "unused green legend",
            "Reserve real space for footnotes",
        ],
        "scripts/svg_layout_smoke_check.py": [
            "long unwrapped text",
            "horizontal canvas bounds",
            "possible text overlap",
            "panel bounds",
        ],
        "scripts/figure_whitespace_smoke_check.py": [
            "content_bbox",
            "large {side} whitespace margin",
            "content occupies only",
            "check-bottom-text",
        ],
        "scripts/figure_code_smoke_check.py": [
            "global lon-lat imshow",
            "fixed 1-5 green-yellow-red risk scale",
            "low fig.text",
            "aspect=aspect",
        ],
        "scripts/figure_scale_smoke_check.py": [
            "unused_low",
            "low-color semantics",
            "observed values use only",
        ],
        "roles/assess.md": [
            "figure_whitespace_smoke_check.py",
            "figure_code_smoke_check.py",
            "figure_scale_smoke_check.py",
            "delivered figure is raster",
        ],
        "roles/draft.md": [
            "content bounding-box balance",
            "third of the canvas blank",
            "semantic palettes",
            "fig.text",
        ],
        "references/target-journal-scorecard.md": [
            "large rendered whitespace imbalance",
            "distorted map aspect",
            "misleading unused semantic colorbar segments",
        ],
    }

    for rel, terms in required_terms.items():
        text = load_text(root / rel)
        missing = [term for term in terms if term not in text]
        if missing:
            fail(f"{rel} is missing figure layout terms: {', '.join(missing)}")


def validate_methods_si_reproducibility_surface(root: Path) -> None:
    required_terms = {
        "references/supplementary-information-audit.md": [
            "Reviewer-Reproducible Methods Gate",
            "Data inputs",
            "Preprocessing",
            "Notation",
            "Equations",
            "Output crosswalk",
            "scripts/docx_equation_smoke_check.py",
        ],
        "references/journal-structure-audit.md": [
            "zero Office Math objects",
            "scripts/docx_equation_smoke_check.py",
        ],
        "references/manuscript-heuristics.md": [
            "zero Office Math objects",
            "references/supplementary-information-audit.md",
        ],
        "roles/assess.md": [
            "package-cleanliness checks",
            "Office Math objects",
        ],
        "roles/draft.md": [
            "formal equations/predicates",
            "Office Math",
        ],
        "roles/journal.md": [
            "Methods/SI reproducibility gate",
            "thin Methods",
        ],
        "scripts/docx_equation_smoke_check.py": [
            "oMath",
            "formula_like_hits",
        ],
    }

    for rel, terms in required_terms.items():
        text = load_text(root / rel)
        missing = [term for term in terms if term not in text]
        if missing:
            fail(f"{rel} is missing Methods/SI reproducibility terms: {', '.join(missing)}")


def main() -> None:
    root = Path(sys.argv[1]).expanduser().resolve() if len(sys.argv) > 1 else Path.cwd().resolve()
    if not root.exists() or not root.is_dir():
        fail(f"skill path does not exist: {root}")

    validate_required_files(root)
    validate_skill_md(root)
    validate_openai_yaml(root)
    validate_referenced_paths(root)
    validate_long_markdown_navigation(root)
    validate_source_packaging_note(root)
    validate_managed_harness_surface(root)
    validate_parameter_provenance_surface(root)
    validate_target_journal_scorecard_surface(root)
    validate_target_journal_scorecard_points(root)
    validate_score_calibration_surface(root)
    validate_figure_layout_surface(root)
    validate_methods_si_reproducibility_surface(root)
    print(f"OK: {root}")


if __name__ == "__main__":
    main()
