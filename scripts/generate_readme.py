#!/usr/bin/env python3
"""Regenerate README.md from data/taxonomy.yml + data/papers.yml.

Single source of truth: edit the YAML, run this script, commit the README.
The matrix cells link down into per-(stage x objective) detail sections, so
the overview and the paper list can never drift apart.

    python3 scripts/generate_readme.py

Requires: PyYAML  (pip install pyyaml)
"""
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


def github_slug(text: str) -> str:
    """Replicate GitHub's heading -> anchor algorithm.

    lowercase; drop everything except [a-z0-9], hyphen, underscore and space;
    spaces -> hyphens. (No dedup handling — our headings are unique.)
    """
    text = text.strip().lower()
    text = re.sub(r"[^\w\- ]", "", text, flags=re.UNICODE)  # \w keeps letters/digits/_
    text = re.sub(r"[^a-z0-9_\- ]", "", text)  # ...but restrict letters to ascii
    return text.replace(" ", "-")


def load():
    tax = yaml.safe_load((DATA / "taxonomy.yml").read_text())
    papers = yaml.safe_load((DATA / "papers.yml").read_text())["papers"]
    tools_path = DATA / "tools.yml"
    tools = (yaml.safe_load(tools_path.read_text()) or {}).get("tools", []) if tools_path.exists() else []
    return tax, papers, tools


def cell_papers(papers, stage_id, objective):
    return [
        p for p in papers
        if p["stage"] == stage_id and objective in p.get("objectives", [])
    ]


def kind_counts(entries, kinds):
    """Ordered '🗡️2 🛡️1' string for the kinds present in `entries`."""
    parts = []
    for k, meta in kinds.items():
        n = sum(1 for e in entries if e.get("kind") == k)
        if n:
            parts.append(f"{meta['emoji']}{n}")
    return " ".join(parts)


def sort_key(p):
    # newest first, then title
    return (-int(p.get("year", 0)), p.get("title", ""))


def render_entry(p, kinds, cat=None):
    emoji = kinds.get(p.get("kind"), {}).get("emoji", "•")
    cat_e = f"{cat['emoji']} " if cat else ""
    title = p["title"]
    link = p.get("code") or p.get("paper") or p.get("project") or ""
    head = f"[{title}]({link})" if link else title
    line = [f"- {emoji} {cat_e}**{head}**"]
    if p.get("tldr"):
        line.append(f" — {p['tldr']}")
    line.append("  ")  # markdown line break
    meta = []
    authors = p.get("authors")
    venue_year = " ".join(str(x) for x in [p.get("venue"), p.get("year")] if x)
    byline = ". ".join(x for x in [f"_{authors}_" if authors else "", venue_year] if x)
    if byline:
        meta.append(byline)
    links = []
    if p.get("paper"):
        links.append(f"[📄 paper]({p['paper']})")
    if p.get("code"):
        links.append(f"[💻 code]({p['code']})")
    if p.get("project"):
        links.append(f"[🌐 project]({p['project']})")
    if links:
        meta.append(" · ".join(links))
    if p.get("domains"):
        meta.append(" ".join(f"`{d}`" for d in p["domains"]))
    line.append("\n  " + "  \n  ".join(meta))
    return "".join(line)


def render_tool(t, tool_types, cat=None):
    emoji = tool_types.get(t.get("type"), {}).get("emoji", "•")
    cat_e = f"{cat['emoji']} " if cat else ""
    line = [f"- {emoji} {cat_e}**[{t['name']}]({t['url']})**"]
    if t.get("tldr"):
        line.append(f" — {t['tldr']}")
    meta = []
    tlabel = tool_types.get(t.get("type"), {}).get("label")
    if tlabel:
        meta.append(tlabel)
    if t.get("domains"):
        meta.append(" ".join(f"`{d}`" for d in t["domains"]))
    if meta:
        line.append("  \n  " + " · ".join(meta))
    return "".join(line)


def build(tax, papers, tools):
    stages = tax["stages"]
    objectives = tax["objectives"]
    kinds = tax["kinds"]
    obj_emoji = {
        "Confidentiality": "🔒",
        "Integrity": "🧬",
        "Availability": "⚡",
        "Safety": "🚦",
    }
    stage_label = {s["id"]: s["label"] for s in stages}
    categories = tax.get("categories", [])
    cat_by_id = {c["id"]: c for c in categories}
    cat_priority = tax.get("category_priority", [c["id"] for c in categories])
    fallback_cat = {"id": "general", "emoji": "⚙️", "label": "Cross-cutting"}

    def category_of(p):
        cid = p.get("category")
        if not cid:
            doms = set(p.get("domains", []))
            cid = next(
                (c for c in cat_priority
                 if doms & set(cat_by_id.get(c, {}).get("match", []))),
                "general",
            )
        return cat_by_id.get(cid, fallback_cat)

    total = len(papers)
    with_code = sum(1 for p in papers if p.get("code"))
    n_attack = sum(1 for p in papers if p.get("kind") == "attack")
    n_defense = sum(1 for p in papers if p.get("kind") == "defense")

    out = []
    A = out.append

    # ── Header ────────────────────────────────────────────────────────────
    A("# Awesome Security of Physical AI [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)\n")
    A(
        "> A curated, **papers-with-code** map of security & safety research for "
        "**Physical AI** — autonomous vehicles, drones, robots, and embodied "
        "LLM/VLA agents — organized as a **pipeline stage × security objective** matrix.\n"
    )
    A(
        f"![papers](https://img.shields.io/badge/papers-{total}-blue) "
        f"![with code](https://img.shields.io/badge/with%20code-{with_code}-brightgreen) "
        "[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md) "
        "[![suggest a paper](https://img.shields.io/badge/suggest-a%20paper-8A2BE2)]"
        "(../../issues/new?template=suggest-a-paper.yml)\n"
    )
    A("**New here?** Read the [contributing guide](CONTRIBUTING.md) or "
      "[suggest a paper](../../issues/new?template=suggest-a-paper.yml) — no git required.\n")

    # ── Legend ────────────────────────────────────────────────────────────
    A("## How to read this list\n")
    A(
        "Every paper sits at one **pipeline stage** (row) and targets one or more "
        "**security objectives** (column). Each matrix cell shows how many papers "
        "of each kind land there and links to the details below.\n"
    )
    A("**Kinds** — " + " · ".join(f"{m['emoji']} {m['label']}" for m in kinds.values()) + "\n")
    A(
        "**Objectives** — 🔒 Confidentiality (don't leak model/data) · "
        "🧬 Integrity (don't get fooled/poisoned) · "
        "⚡ Availability (stay up under DoS) · "
        "🚦 Safety (don't take unsafe physical action)\n"
    )
    if categories:
        A("**Platform** — " + " · ".join(
            f"{c['emoji']} {c['label']}" for c in categories) + "\n")
    A("**Links** — 📄 paper · 💻 code · 🌐 project page\n")

    # ── Matrix ────────────────────────────────────────────────────────────
    A("## The matrix\n")
    header = "| Stage \\ Objective | " + " | ".join(
        f"{obj_emoji.get(o, '')} {o}" for o in objectives
    ) + " |"
    sep = "|" + " --- |" * (len(objectives) + 1)
    A(header)
    A(sep)
    for s in stages:
        row = [f"**{s['label']}**"]
        for o in objectives:
            entries = cell_papers(papers, s["id"], o)
            if entries:
                counts = kind_counts(entries, kinds) or str(len(entries))
                anchor = github_slug(f"{s['label']} · {o}")
                row.append(f"[{counts}](#{anchor})")
            else:
                row.append("—")
        A("| " + " | ".join(row) + " |")
    lines = out  # noqa
    A("")
    A("<sub>Cells count papers by kind; click a cell to jump to its section. "
      "“—” = gap we haven't mapped yet (PRs very welcome).</sub>\n")

    # ── ⭐ Papers with code (the highlight reel) ───────────────────────────
    coded = sorted([p for p in papers if p.get("code")], key=sort_key)
    A("## ⭐ Papers with code\n")
    A("The reason this list exists — every row ships a public implementation.\n")
    A("| Paper | Platform | Stage | Objectives | Venue | Code |")
    A("| --- | --- | --- | --- | --- | --- |")
    for p in coded:
        objs = " ".join(obj_emoji.get(o, o) for o in p.get("objectives", []))
        emoji = kinds.get(p.get("kind"), {}).get("emoji", "•")
        cat = category_of(p)
        vy = " ".join(str(x) for x in [p.get("venue"), p.get("year")] if x)
        A(
            f"| {emoji} [{p['title']}]({p.get('paper') or p['code']}) "
            f"| {cat['emoji']} {cat['label']} "
            f"| {stage_label.get(p['stage'], p['stage'])} | {objs} | {vy} "
            f"| [💻]({p['code']}) |"
        )
    A("")

    # ── Browse by domain ─────────────────────────────────────────────────
    by_domain: dict[str, list] = {}
    for p in papers:
        for d in p.get("domains", []):
            by_domain.setdefault(d, []).append(p)
    A("## Browse by domain\n")
    for d in sorted(by_domain):
        items = sorted(by_domain[d], key=sort_key)
        links = ", ".join(
            f"[{p['title'].split(':')[0].split('(')[0].strip()}]"
            f"({p.get('code') or p.get('paper') or p.get('project')})"
            for p in items
        )
        A(f"- **`{d}`** ({len(items)}) — {links}")
    A("")

    # ── Details ───────────────────────────────────────────────────────────
    A("## Papers by stage\n")
    for s in stages:
        stage_entries = [p for p in papers if p["stage"] == s["id"]]
        if not stage_entries:
            continue
        A(f"### {s['label']}\n")
        if s.get("desc"):
            A(f"_{s['desc']}_\n")
        for o in objectives:
            entries = sorted(cell_papers(stage_entries, s["id"], o), key=sort_key)
            if not entries:
                continue
            # NB: heading text must stay in sync with github_slug() call above.
            A(f"#### {s['label']} · {o}\n")
            for p in entries:
                A(render_entry(p, kinds, category_of(p)))
            A("")

    # ── Open-source tools (same axes) ─────────────────────────────────────
    tool_types = tax.get("tool_types", {})
    if tools:
        A("## Open-source tools\n")
        A("Reusable tooling on the **same axes** — to build, attack, defend, "
          "simulate and stress-test physical-AI systems.\n")
        A("**Types** — " + " · ".join(
            f"{m['emoji']} {m['label']}" for m in tool_types.values()) + "\n")
        # matrix
        A(header)
        A(sep)
        for s in stages:
            row = [f"**{s['label']}**"]
            for o in objectives:
                cell = [t for t in tools
                        if t["stage"] == s["id"] and o in t.get("objectives", [])]
                if cell:
                    parts = []
                    for tid, meta in tool_types.items():
                        n = sum(1 for t in cell if t.get("type") == tid)
                        if n:
                            parts.append(f"{meta['emoji']}{n}")
                    counts = " ".join(parts) or str(len(cell))
                    anchor = github_slug(f"Tools: {s['label']} · {o}")
                    row.append(f"[{counts}](#{anchor})")
                else:
                    row.append("—")
            A("| " + " | ".join(row) + " |")
        A("")
        # details
        for s in stages:
            stage_tools = [t for t in tools if t["stage"] == s["id"]]
            if not stage_tools:
                continue
            for o in objectives:
                entries = sorted(
                    [t for t in stage_tools if o in t.get("objectives", [])],
                    key=lambda t: t["name"].lower(),
                )
                if not entries:
                    continue
                # NB: heading text must stay in sync with the github_slug() call above.
                A(f"### Tools: {s['label']} · {o}\n")
                for t in entries:
                    A(render_tool(t, tool_types, category_of(t)))
                A("")

    # ── Footer ────────────────────────────────────────────────────────────
    A("## Stats\n")
    A(f"- **{total}** papers — 🗡️ {n_attack} attacks, 🛡️ {n_defense} defenses.")
    pct = round(100 * with_code / total) if total else 0
    A(f"- **{with_code}/{total}** ({pct}%) ship public **code**.")
    if categories:
        counts = {c["id"]: 0 for c in categories}
        for p in papers:
            counts[category_of(p)["id"]] = counts.get(category_of(p)["id"], 0) + 1
        line = " · ".join(
            f"{c['emoji']} {c['label']} {counts.get(c['id'], 0)}"
            for c in categories if counts.get(c["id"], 0)
        )
        A(f"- By platform — {line}.")
    if tools:
        A(f"- Plus **{len(tools)}** open-source tools.")
    A("")
    A("## Contributing\n")
    A(
        "Contributions are welcome — this list is only as good as the community "
        "keeps it. **Two ways in:**\n"
    )
    A(
        "- 💬 **Suggest a paper** (no git needed): open a "
        "[paper-suggestion issue](../../issues/new?template=suggest-a-paper.yml) "
        "with the title, venue and links.\n"
        "- 🔧 **Open a pull request**: add your entry to "
        "[`data/papers.yml`](data/papers.yml) (or a tool to "
        "[`data/tools.yml`](data/tools.yml)), run "
        "`python3 scripts/generate_readme.py`, and commit **both** the YAML and the "
        "regenerated `README.md`. CI fails if the README is stale.\n"
    )
    A(
        "House rules: prioritize **papers with public code**, keep entries in scope "
        "(security/safety of physical or embodied AI), and never edit `README.md` by "
        "hand. Full guide → [CONTRIBUTING.md](CONTRIBUTING.md).\n"
    )
    A("## License\n")
    A("[CC0-1.0](LICENSE) — to the extent possible under law, dedicated to the public domain.\n")

    A(f"<sub>Generated by `scripts/generate_readme.py` on {date.today().isoformat()}. Do not edit README.md by hand.</sub>")

    return "\n".join(out) + "\n"


def main():
    tax, papers, tools = load()
    # basic validation
    stage_ids = {s["id"] for s in tax["stages"]}
    valid_obj = set(tax["objectives"])
    valid_kind = set(tax["kinds"])
    valid_type = set(tax.get("tool_types", {}))
    errors = []
    for p in papers:
        if p.get("stage") not in stage_ids:
            errors.append(f"{p.get('title')!r}: bad stage {p.get('stage')!r}")
        for o in p.get("objectives", []):
            if o not in valid_obj:
                errors.append(f"{p.get('title')!r}: bad objective {o!r}")
        if p.get("kind") not in valid_kind:
            errors.append(f"{p.get('title')!r}: bad kind {p.get('kind')!r}")
    for t in tools:
        if t.get("stage") not in stage_ids:
            errors.append(f"tool {t.get('name')!r}: bad stage {t.get('stage')!r}")
        for o in t.get("objectives", []):
            if o not in valid_obj:
                errors.append(f"tool {t.get('name')!r}: bad objective {o!r}")
        if t.get("type") not in valid_type:
            errors.append(f"tool {t.get('name')!r}: bad type {t.get('type')!r}")
    if errors:
        print("Validation errors:\n  " + "\n  ".join(errors), file=sys.stderr)
        sys.exit(1)
    (ROOT / "README.md").write_text(build(tax, papers, tools))
    print(f"Wrote README.md — {len(papers)} papers "
          f"({sum(1 for p in papers if p.get('code'))} with code), {len(tools)} tools.")


if __name__ == "__main__":
    main()
