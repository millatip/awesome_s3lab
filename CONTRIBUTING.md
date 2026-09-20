# Contributing

Thanks for helping map the security of Physical AI! This list is **generated**,
so you never edit `README.md` directly.

## Add or edit a paper

1. Open [`data/papers.yml`](data/papers.yml) and add an entry:

   ```yaml
   - title: "Paper title (short alias)"
     authors: "First A, Second B, Third C"
     venue: "IEEE S&P"          # conference/journal, or "arXiv"
     year: 2025
     stage: inference            # one id from data/taxonomy.yml
     objectives: [Integrity, Safety]   # one+ of Confidentiality/Integrity/Availability/Safety
     kind: attack                # attack | defense | benchmark | survey
     domains: [autonomous-driving, lidar]   # free-form tags
     tldr: "One sentence on what it does."
     paper: "https://arxiv.org/abs/...."
     code: "https://github.com/....."       # OMIT if there is no public repo
     project: "https://...."                # optional website when there's no code
     # category: robot                      # optional override; usually inferred from domains
   ```

   The **Platform** column (🚗 AV · 🚁 Drone/UAV · 🦾 Robot · 🤖 Embodied LLM/VLA ·
   ⚙️ Cross-cutting) is inferred automatically from your `domains` tags — add a tag
   like `drone`, `vla`, or `autonomous-driving` and it classifies itself. Only set
   an explicit `category:` id (from `data/taxonomy.yml`) when the inference is wrong.

2. Regenerate and check:

   ```bash
   python3 scripts/generate_readme.py
   ```

3. Commit **both** the YAML change and the regenerated `README.md`.

## Rules of thumb

- **Code is the point.** Add the `code:` field only when a public implementation
  actually exists — that's what makes this list useful. When in doubt, leave it out
  and use `project:` for a website/demo.
- **One primary `stage`** per paper (the stage the work is really about). A paper can
  target **several `objectives`** — it will then appear in each relevant matrix cell.
- Keep `tldr` to a single, concrete sentence (what the attack/defense does).
- Prefer a stable link: arXiv abstract page, the publisher DOI, or the USENIX/ IEEE page.
- New pipeline stage, objective, or kind? Edit [`data/taxonomy.yml`](data/taxonomy.yml).

## Scope

In scope: security, privacy, and safety of **physical / embodied AI** — autonomous
driving, drones/UAVs, robotics & manipulation, cyber-physical control, and embodied
LLM/VLA agents that take real-world actions. Purely digital ML security with no
physical/embodied angle is out of scope (there are other great lists for that).
