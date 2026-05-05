# Task goal
Add support for BLOCKED tasks in the task summary output.
Update tests and run them.
Leave parser edge cases for the next session.

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