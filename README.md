# Capstone: ship a real tool, with tests, CI and Docker


> **Darsi briefs are short on purpose.** The in-app lesson shows tight numbered clicks. This README keeps the full commands, error fixes, and background for each milestone — open the matching **Milestone N** section when you need detail.

Build a marks-and-attendance tool a teacher could use: test-first Python, a Typer CLI and bilingual HTML report, GitHub Actions with a coverage floor, a Docker image, and a tagged release.

[العربية](README.ar.md)

## What you will be able to do

- Run real free tools from a laptop or Codespaces
- Finish five milestones, each with checks you can self-verify
- Leave with a portfolio piece: a report, demo or tool tagged v1.0
- **Darsi never runs your code** — it reads your link and check file, then an advisory review

## Install once

### Windows

1. Install Python 3.12: open PowerShell and run winget install Python.Python.3.12
2. Install Git: winget install Git.Git
3. Install VS Code from https://code.visualstudio.com (free)
4. On GitHub, open https://github.com/darsi-org/code-capstone and press Use this template, then Clone your copy
5. In the project folder run:
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   python check.py

### Mac

1. Install Homebrew from https://brew.sh if you don't have it
2. brew install python@3.12 git
3. Install VS Code from https://code.visualstudio.com
4. On GitHub open https://github.com/darsi-org/code-capstone → Use this template → clone your copy
5. In the project folder run:
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   python check.py

### Codespaces / Colab

No computer of your own? Use GitHub Codespaces: open your copy → Code → Codespaces → Create codespace. Everything installs there. Or open a notebook in Google Colab, run the first cell that clones your repo, then run python check.py. Both work from a borrowed laptop; a phone browser is enough to read results.

## Start

Press **Use this template** on https://github.com/darsi-org/code-capstone, clone your copy, then follow milestone 1.

## Milestones

### m1: Plan it like a team (2 hours)

## Why this matters
Real software starts with who it is for and what it will never do — especially with pupil data.

## Tools for this milestone
- **GitHub Issues / docs/STORIES.md** — six user stories. Get it: free on GitHub
- **sample.csv** — 30 made-up pupils. Get it: scripts/make_sample.py

## Do this
1. Clone https://github.com/darsi-org/code-capstone, set up venv, run: python scripts/make_sample.py
2. Write six user stories in docs/STORIES.md (and as GitHub issues): who, what, why.
3. README: what it does, how to run in ≤3 commands, what it will never do (no real grades leave the teacher's computer).
4. Run python check.py --milestone m1.

## You know you're done when
- sample.csv exists
- STORIES.md has 6 stories
- m1 passes

## If something goes wrong
- **Stories are just feature names** → Rewrite as: As a teacher, I want… so that…
- **Real pupil names in sample** → Regenerate with make_sample.py; never paste class lists

## What you should understand
You can plan a tool with stories and hard privacy limits before writing code.

**Hand in:** Six stories, README, sample.csv, and darsi-check.json that passes m1.

### m2: The core, tests first (4 hours)

## Why this matters
Write the test, watch it fail, then make it pass. Edge cases are where bugs hide.

## Tools for this milestone
- **pytest + pytest-cov** — tests and coverage. Get it: in requirements.txt
- **ruff** — fast linter. Get it: in requirements.txt

## Do this
1. In marks/core.py implement load, averages, at_risk, clean_id — but write failing tests in tests/test_core.py first.
2. Cover edges: blank ID, repeated ID, mark 105, Arabic names, empty file.
3. Run: pytest --cov=marks --cov-fail-under=80 && ruff check . && python check.py --milestone m2

## You know you're done when
- ≥8 core tests
- Coverage ≥80%
- m2 passes

## If something goes wrong
- **Coverage below 80** → Add tests for except branches and empty input
- **Mark 105 crashes** → Report the bad row; keep it out of averages

## What you should understand
You can grow core logic test-first and refuse silent bad data.

**Hand in:** marks/core.py, tests, coverage report, and darsi-check.json that passes m2.

### m3: A command line and a bilingual report (4 hours)

## Why this matters
A tool nobody else can run is unfinished. Arabic RTL reports need dir and isolation.

## Tools for this milestone
- **Typer** — builds CLI with --help. Get it: in requirements.txt
- **CliRunner** — tests the CLI. Get it: from typer.testing

## Do this
1. In marks/cli.py add: marks summary sample.csv and marks report sample.csv --lang ar --out report.html.
2. HTML report: averages, at-risk pupils, dir=rtl for Arabic, <bdi> for mixed bits.
3. Save examples/report-en.html and examples/report-ar.html. Test with CliRunner. Run pytest && python check.py --milestone m3.

## You know you're done when
- Typer CLI exists
- Two example reports
- m3 passes

## If something goes wrong
- **Arabic names reversed next to numbers** → Set dir=rtl and wrap mixed spans in <bdi>
- **marks command not found** → pip install -e . so the script entry point installs

## What you should understand
You can ship a CLI and an RTL-aware report that a teacher can open.

**Hand in:** marks/cli.py, example reports, CLI tests, and darsi-check.json that passes m3.

### m4: Continuous integration on GitHub Actions (2 hours)

## Why this matters
A robot that checks every push keeps the safety net from wearing thin.

## Tools for this milestone
- **GitHub Actions** — runs ruff and pytest with coverage floor. Get it: free for public repos

## Do this
1. Edit ci.yml: on push/PR, install, ruff check ., pytest --cov=marks --cov-fail-under=80.
2. Push a change that breaks a test on purpose, watch red, then fix to green. Add the CI badge to README.
3. Run python check.py --milestone m4.

## You know you're done when
- ci.yml has cov-fail-under and ruff
- m4 passes

## If something goes wrong
- **Actions not running** → Settings → Actions → allow; push to default branch
- **Coverage flake** → Pin the seed and avoid depending on dict order

## What you should understand
You can make every push prove lint and tests still pass.

**Hand in:** ci.yml, red then green links, badge, and darsi-check.json that passes m4.

### m5: Docker and release v1.0 (3 hours)

## Why this matters
Docker ends 'works on my machine'. A changelog lets people know what v1.0 means.

## Tools for this milestone
- **Docker** — python:3.12-slim image that runs marks. Get it: Dockerfile in the starter

## Do this
1. Finish Dockerfile: WORKDIR, COPY, pip install ., ENTRYPOINT marks. Test: docker build -t marks . && docker run --rm -v %cd%/data:/data marks report /data/sample.csv --out /data/report.html
2. Add a CI job that builds the image. Write CHANGELOG.md. Close finished stories. Tag v1.0.
3. Run python check.py --milestone m5. Explain on Darsi.

## You know you're done when
- Dockerfile has ENTRYPOINT
- CHANGELOG.md exists
- m5 passes

## If something goes wrong
- **Docker permission errors on Windows** → Share the drive in Desktop settings; use ${PWD} carefully in PowerShell
- **Image missing sample data** → Mount a volume; don't bake real data into the image

## What you should understand
You can package a tool so anyone runs the same command and cite a version.

**Hand in:** Dockerfile, green image build, CHANGELOG.md, v1.0, darsi-check.json that passes m5, and your explanation.

## The check

Run `python check.py` or `python check.py --milestone m2`. It only reads files, writes `darsi-check.json`, and prints English and Arabic. It uploads nothing.

## Review on Darsi

Send your repository link and `darsi-check.json` with each milestone on Darsi. Darsi reads your latest Actions run and release from GitHub's public API, adds an advisory AI review, then your teacher or the Darsi team reviews it. **Darsi never runs your code.**

## Licence

MIT — see [LICENSE](LICENSE).
