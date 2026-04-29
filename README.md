# AICTX Demo Taskflow

A small, functional Python project for demonstrating AICTX session continuity.

The project is intentionally simple: it parses task files and prints a status summary.
It is not just scaffolding. It has a working package, CLI, tests, examples, and demo prompts.

```text
Quick start.
Session 1 leaves context.
Session 2 resumes from it.
Cleanup.
```

## Why this repo exists

AICTX is easiest to understand when you see a new coding-agent session resume from the repo's last operational state instead of starting from zero.

This repo gives you a controlled demo target:

- baseline code works;
- tests pass;
- `TODO` and `DONE` are supported;
- `BLOCKED` is intentionally unsupported in v0.1.0;
- session 1 can add `BLOCKED` support;
- session 2 can resume from the AICTX handoff and validate edge cases.

## Project structure

```text
aictx-demo-taskflow/
  pyproject.toml
  README.md
  src/taskflow/
    cli.py
    models.py
    parser.py
    summary.py
  tests/
    test_cli.py
    test_parser.py
    test_summary.py
  examples/
    tasks.txt
    session_1_target.txt
  docs/
    DEMO_FLOW.md
    SESSION_PROMPTS.md
    EXPECTED_OUTPUTS.md
```

## Local setup

Recommended for the demo:

```bash
make test
```

`make test` creates a local `.venv`, installs the package in editable mode with development dependencies, and runs `pytest`.

Use a specific Python if needed:

```bash
make test PYTHON=python3.12
```

Manual equivalent:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
python -m pytest -q
```

Useful targets:

```bash
make run
make demo-target
make ci
make clean
```

## Run the CLI

```bash
python -m taskflow.cli examples/tasks.txt
```

Expected output:

```text
todo: 2
done: 1
total: 3
```

You can also use the installed console script after editable install:

```bash
taskflow examples/tasks.txt
```

## Baseline limitation for the demo

This file contains a `BLOCKED` task:

```bash
python -m taskflow.cli examples/session_1_target.txt
```

Before session 1, this should fail with an unsupported status error. That is intentional.

The first coding-agent session should add `BLOCKED` support and leave AICTX continuity for the next session.

## AICTX quick start for the video

From this repo:

```bash
pip install aictx
aictx install
aictx init
aictx --version
```

Then show what AICTX added:

```bash
find . -maxdepth 2 -name '.aictx' -o -name 'AGENTS.md' -o -name 'CLAUDE.md' -o -name '.claude'
```

## Session 1 prompt

```text
Add support for BLOCKED tasks in the task summary output. Update the parser, summary, CLI tests, and examples. Run the tests. Leave a clear AICTX handoff so the next session can validate blocked task edge cases.
```

## Session 2 prompt

```text
Continue from the AICTX startup banner and validate the blocked task parsing edge cases left by the previous session.
```

## Cleanup

Repo-local cleanup:

```bash
aictx clean --repo .
```

Optional global cleanup:

```bash
aictx uninstall
```

## Video message

```text
AICTX is not another coding agent.
It is repo-local continuity for the coding agents you already use.
Stop starting from zero.
```
