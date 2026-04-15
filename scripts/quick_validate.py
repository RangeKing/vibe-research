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
    "references/sentence-level-writing-audit.md",
    "templates/research_task_packet.md",
    "templates/campaign_checkpoint.md",
    "templates/research_memory.md",
    "templates/polish_pass.md",
    "templates/writing_quality_review.md",
]


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


def validate_required_files(root: Path) -> None:
    missing = [rel for rel in EXPECTED_FILES if not (root / rel).exists()]
    if missing:
        fail(f"missing required repository files: {', '.join(missing)}")


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

    packet_text = load_text(root / "templates/research_task_packet.md")
    for field in ["session_state", "frontier", "inputs", "recovery_mode", "merge_target", "stop_conditions"]:
        if field not in packet_text:
            fail(f"templates/research_task_packet.md is missing `{field}`")

    checkpoint_text = load_text(root / "templates/campaign_checkpoint.md")
    for field in ["Last trustworthy state", "Active frontier", "Open loops", "Blocked on", "Next wake instruction"]:
        if field not in checkpoint_text:
            fail(f"templates/campaign_checkpoint.md is missing `{field}`")

    memory_text = load_text(root / "templates/research_memory.md")
    for field in ["Reusable heuristics", "Decision rules", "Killed patterns", "Do not repeat"]:
        if field not in memory_text:
            fail(f"templates/research_memory.md is missing `{field}`")


def main() -> None:
    root = Path(sys.argv[1]).expanduser().resolve() if len(sys.argv) > 1 else Path.cwd().resolve()
    if not root.exists() or not root.is_dir():
        fail(f"skill path does not exist: {root}")

    validate_required_files(root)
    validate_skill_md(root)
    validate_openai_yaml(root)
    validate_managed_harness_surface(root)
    print(f"OK: {root}")


if __name__ == "__main__":
    main()
