# Task goal
Add support for BLOCKED tasks in the task summary output.
Update tests and run them.
Leave parser edge cases for the next session.

# Hard Rules
- When calling aictx, pass only the task goal:
- Do not include reporting instructions, metrics JSON schemas, output-format rules, or this full prompt in the aictx resume --request value.
Correct:

```bash
aictx resume --repo . --request "Add support for BLOCKED tasks in the task summary output. Update tests and run them. Leave parser edge cases for the next session." --json
```

# Reporting instructions
At the end of this session, write `session_1_metrics.json` using this exact JSON shape:

{
  "files_explored": [],
  "files_edited": [],
  "commands_run": [],
  "tests_run": [],
  "next_step_left_for_session_2": "",
  "notes": ""
}

## Reporting Rules:
- `files_explored` includes only files you explicitly opened/read/inspected.
- Do not include generated files.
- Do not include files only touched by tests.
- If unsure, omit the item rather than guessing.