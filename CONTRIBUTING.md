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

## Opening a pull request

The full workflow, start to finish:

1. **Fork** this repo (top-right on GitHub) and **clone** your fork:

   ```bash
   git clone https://github.com/<you>/awesome_s3lab.git
   cd awesome_s3lab
   pip install pyyaml
   ```

2. **Branch** off `main` with a short, descriptive name:

   ```bash
   git checkout -b add-ndss25-drone-papers
   ```

3. **Edit the data**, not the README: add entries to
   [`data/papers.yml`](data/papers.yml) (see the schema above).

4. **Regenerate** and eyeball the result:

   ```bash
   python3 scripts/generate_readme.py
   ```

   The script also validates your entry (stage/objective/kind must exist) and
   fails loudly if something is off.

5. **Commit both files** together — the YAML and the regenerated `README.md`:

   ```bash
   git add data/papers.yml README.md
   git commit -m "Add 3 NDSS'25 drone sensor-spoofing papers"
   git push -u origin add-ndss25-drone-papers
   ```

6. **Open the PR** against `millatip/awesome_s3lab:main`. The PR template's
   checklist appears automatically — tick each box.

7. **CI runs** [`.github/workflows/check-readme.yml`](.github/workflows/check-readme.yml):
   it re-runs the generator and **fails if `README.md` is stale** (i.e. you edited
   the YAML but forgot to regenerate). If it goes red, run step 4 again, commit the
   updated `README.md`, and push — the PR updates itself.

8. A maintainer reviews for scope, correct links, and no duplicates, then merges.

**Tips**

- Keep one topic per PR (e.g. "drone papers" or "fix a broken link") — small PRs
  review fast.
- Verify each `code:` link opens before you push: `curl -sL -o /dev/null -w '%{http_code}\n' <url>` should print `200`.
- Not comfortable with git? Open an **issue** with the paper title, venue/year, and
  links, and someone will add it.

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
