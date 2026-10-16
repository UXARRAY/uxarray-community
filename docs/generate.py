"""Generate the site's entry pages from entries/ before Sphinx reads the sources.

Each entry folder is copied to docs/entries/<slug>/ and given an index.md built from
its README metadata, README body, and notebooks. docs/entries/index.md is the catalog.
Everything under docs/entries/ is regenerated on every build and is git-ignored.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent
ROOT = DOCS.parent
OUT = DOCS / "entries"

sys.path.insert(0, str(ROOT / "scripts"))
from build_index import ENTRIES, FRONT_MATTER_RE, cell, collect  # noqa: E402

IGNORE = shutil.ignore_patterns(".ipynb_checkpoints", "__pycache__", ".DS_Store")


def entry_page(entry: dict, folder: Path) -> str:
    readme = (folder / "README.md").read_text(encoding="utf-8")
    body = FRONT_MATTER_RE.sub("", readme, count=1).strip()

    authors = ", ".join(
        f"[@{a.lstrip('@')}](https://github.com/{a.lstrip('@')})" for a in entry["authors"]
    )
    facts = [
        f"**Date:** {entry['date'].isoformat()}",
        f"**Type:** {entry['type']}",
        f"**Authors:** {authors}",
        f"**UXarray:** {entry['uxarray_version']}",
    ]
    if entry["tags"]:
        facts.append("**Tags:** " + " ".join(f"`{t}`" for t in entry["tags"]))

    lines = [f"# {entry['title']}", ""]
    if entry["status"] == "superseded":
        lines += [
            ":::{warning}",
            "This entry is superseded. See its description for the newer approach.",
            ":::",
            "",
        ]
    lines += [" · ".join(facts), "", body, ""]

    notebooks = sorted(
        p.relative_to(folder).with_suffix("").as_posix()
        for p in folder.rglob("*.ipynb")
        if ".ipynb_checkpoints" not in p.parts
    )
    if notebooks:
        lines += ["```{toctree}", ":maxdepth: 1", ":titlesonly:", ":caption: Notebooks", "", *notebooks, "```", ""]

    # Other Markdown files (e.g. data.md) are pages too; keep them out of the sidebar.
    others = sorted(
        p.relative_to(folder).with_suffix("").as_posix()
        for p in folder.rglob("*.md")
        if p.name != "README.md" and ".ipynb_checkpoints" not in p.parts
    )
    if others:
        lines += ["```{toctree}", ":hidden:", "", *others, "```", ""]
    return "\n".join(lines)


def catalog(entries: list[dict]) -> str:
    lines = ["# Catalog", "", f"{len(entries)} entries, newest first.", ""]
    entries = sorted(entries, key=lambda e: (e["date"], e["path"]), reverse=True)
    for year in sorted({e["date"].year for e in entries}, reverse=True):
        lines += [
            f"## {year}",
            "",
            "| Date | Title | Type | Authors | UXarray |",
            "|------|-------|------|---------|---------|",
        ]
        for e in (e for e in entries if e["date"].year == year):
            slug = Path(e["path"]).name
            title = f"[{cell(e['title'])}]({slug}/index.md)"
            if e["status"] == "superseded":
                title = f"~~{title}~~ (superseded)"
            authors = ", ".join(f"@{a.lstrip('@')}" for a in e["authors"])
            lines.append(
                f"| {e['date'].isoformat()} | {title} | {e['type']} | {authors} "
                f"| {cell(e['uxarray_version'])} |"
            )
        lines.append("")
    slugs = [f"{Path(e['path']).name}/index" for e in entries]
    lines += ["```{toctree}", ":hidden:", "", *slugs, "```", ""]
    return "\n".join(lines)


def main() -> None:
    entries, errors = collect()
    for err in errors:
        print(f"warning: {err}", file=sys.stderr)

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    for entry in entries:
        src = ENTRIES / Path(entry["path"]).name
        dst = OUT / src.name
        shutil.copytree(src, dst, ignore=IGNORE)
        (dst / "index.md").write_text(entry_page(entry, src), encoding="utf-8")
    (OUT / "index.md").write_text(catalog(entries), encoding="utf-8")


if __name__ == "__main__":
    main()
