# AICTX demo flow

This repository is intentionally small and functional. It is designed to show one thing clearly:

```text
Quick start.
Session 1 leaves context.
Session 2 resumes from it.
Cleanup.
```

## Baseline behavior

The project starts with support for two task statuses:

```text
TODO: record demo
DONE: add tests
```

`BLOCKED` is intentionally unsupported in the baseline. That gives the coding agent a small, safe, understandable task for session 1.

## Quick start scene

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -e '.[dev]'
pytest -q
python -m taskflow.cli examples/tasks.txt
```

Then install and initialize AICTX:

```bash
pip install aictx
aictx install
aictx init
aictx --version
```

Show the scaffolding added by AICTX:

```bash
find . -maxdepth 2 -name '.aictx' -o -name 'AGENTS.md' -o -name 'CLAUDE.md' -o -name '.claude'
```

## Session 1 prompt

```text
Add support for BLOCKED tasks in the task summary output. Update the parser, summary, CLI tests, and examples. Run the tests. Leave a clear AICTX handoff so the next session can validate blocked task edge cases.
```

Expected coding work:

- add `BLOCKED` to `TaskStatus`;
- include `blocked` in `summarize_tasks()`;
- include `blocked` in `format_summary()`;
- update parser/summary/CLI tests;
- make `examples/session_1_target.txt` work;
- leave a next step such as validating whitespace/lowercase edge cases.

## Session 2 prompt

```text
Continue from the AICTX startup banner and validate the blocked task parsing edge cases left by the previous session.
```

Expected viewer takeaway:

```text
The new agent session did not start from zero.
It started from AICTX's repo-local operational state.
```

## Cleanup scene

```bash
aictx clean --repo .
```

Optional full global cleanup:

```bash
aictx uninstall
```

Close the video with the promise, not the cleanup:

```text
AICTX is not another coding agent.
It is repo-local continuity for the coding agents you already use.
Stop starting from zero.
```
