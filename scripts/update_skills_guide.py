#!/usr/bin/env python3
"""
Auto-updates the 产品工作流技能 section in SKILLS_GUIDE.md
when a new SKILL.md is written to d:/claude/skills/.

Triggered by PostToolUse hook on the Write tool.
Reads hook input from stdin (JSON with tool_input.file_path).
"""
import json
import sys
import os
import re
from pathlib import Path

SKILLS_DIR = Path("d:/claude/skills")
GUIDE_PATH = Path("d:/claude/SKILLS_GUIDE.md")
START_MARKER = "<!-- AUTO_UPDATE_START -->"
END_MARKER = "<!-- AUTO_UPDATE_END -->"

# Skills to skip (not actual skill dirs)
SKIP_DIRS = {"备份技能", "claude-code", "skill-router-mcp", "frontend-design"}


def main():
    # Read hook input from stdin
    try:
        raw = sys.stdin.read()
        hook_input = json.loads(raw) if raw.strip() else {}
    except Exception:
        hook_input = {}

    file_path = (
        hook_input.get("tool_input", {}).get("file_path", "")
        or hook_input.get("file_path", "")
    )

    # Only run when a SKILL.md inside the skills directory is written
    normalized = file_path.replace("\\", "/").lower()
    if "skills/" not in normalized or not normalized.endswith("skill.md"):
        return

    skills = scan_skills()
    if not skills:
        sys.stdout.buffer.write(b"[SKIP] No skills found.\n")
        return

    update_guide(skills)


def scan_skills():
    if not SKILLS_DIR.exists():
        return []

    skills = []
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir() or skill_dir.name in SKIP_DIRS:
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue

        try:
            content = skill_md.read_text(encoding="utf-8")
        except Exception:
            continue

        name, description = parse_frontmatter(content)
        if not name:
            name = skill_dir.name

        keywords = extract_keywords(description)
        main_desc = split_description(description)

        skills.append({
            "dir_name": skill_dir.name,
            "name": name,
            "main_desc": main_desc,
            "keywords": keywords,
        })

    return skills


def parse_frontmatter(content):
    name = ""
    description = ""
    if not content.startswith("---"):
        return name, description
    end = content.find("---", 3)
    if end < 0:
        return name, description
    for line in content[3:end].splitlines():
        if line.startswith("name:"):
            name = line[5:].strip()
        elif line.startswith("description:"):
            description = line[12:].strip()
    return name, description


def split_description(description):
    """Return the Chinese part before 'Use when'."""
    idx = description.find("Use when")
    if idx > 0:
        return description[:idx].strip()
    return description.strip()


def extract_keywords(description):
    """Extract trigger keywords from the description string."""
    # Match "Use when the user asks for X, Y, Z"
    m = re.search(r"Use when the user asks for ([^.]+)", description)
    if m:
        raw = m.group(1)
        parts = [k.strip() for k in re.split(r"[,，]", raw) if k.strip()]
        # Keep only Chinese/short tokens, drop long English sentences
        return [p for p in parts if len(p) < 30][:6]
    # Match Chinese "当用户..." pattern
    m = re.search(r"当用户[^，,。.]*[，,]([^。.]+)", description)
    if m:
        raw = m.group(1)
        return [k.strip() for k in re.split(r"[,，]", raw) if k.strip()][:6]
    return []


def generate_section(skills):
    lines = []
    for s in skills:
        lines.append(f"### {s['dir_name']}")
        lines.append("")
        if s["main_desc"]:
            lines.append(f"**功能**：{s['main_desc']}")
            lines.append("")
        if s["keywords"]:
            lines.append(f"**触发关键词**：{' / '.join(s['keywords'])}")
            lines.append("")
        lines.append(f"**调用方式**：`/{s['dir_name']}`")
        lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines)


def update_guide(skills):
    if not GUIDE_PATH.exists():
        sys.stdout.buffer.write(f"[SKIP] Guide not found at {GUIDE_PATH}.\n".encode("utf-8"))
        return

    content = GUIDE_PATH.read_text(encoding="utf-8")
    start_idx = content.find(START_MARKER)
    end_idx = content.find(END_MARKER)

    if start_idx == -1 or end_idx == -1:
        sys.stdout.buffer.write(b"[SKIP] Markers not found in guide.\n")
        return

    new_section = generate_section(skills)
    new_content = (
        content[: start_idx + len(START_MARKER)]
        + "\n\n"
        + new_section
        + "\n"
        + content[end_idx:]
    )

    GUIDE_PATH.write_text(new_content, encoding="utf-8")
    sys.stdout.buffer.write(f"[OK] SKILLS_GUIDE.md updated - {len(skills)} skills listed.\n".encode("utf-8"))


if __name__ == "__main__":
    main()
