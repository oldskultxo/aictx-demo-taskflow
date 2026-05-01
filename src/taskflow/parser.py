from __future__ import annotations

from collections.abc import Iterable

from .models import Task, TaskStatus


class TaskParseError(ValueError):
    """Raised when a task line cannot be parsed."""


def _normalize_line(raw_line: str) -> str:
    line = raw_line.strip()
    if line.startswith("\ufeff"):
        line = line.removeprefix("\ufeff").strip()
    return line


def parse_task_line(raw_line: str, *, line_number: int | None = None) -> Task | None:
    """Parse one task line.

    Accepted baseline format:
        TODO: write quickstart
        DONE: add tests

    Blank lines and comments starting with ``#`` are ignored and return None.
    """

    line = _normalize_line(raw_line)
    if not line or line.startswith("#"):
        return None
    if ":" not in line:
        raise TaskParseError(_message("missing ':' separator", raw_line, line_number))

    raw_status, raw_title = line.split(":", 1)
    status_text = raw_status.strip().upper()
    title = raw_title.strip()

    if not title:
        raise TaskParseError(_message("task title cannot be empty", raw_line, line_number))

    try:
        status = TaskStatus(status_text)
    except ValueError as exc:
        allowed = ", ".join(item.value for item in TaskStatus)
        raise TaskParseError(
            _message(f"unsupported task status '{status_text}' (expected: {allowed})", raw_line, line_number)
        ) from exc

    return Task(status=status, title=title)


def parse_tasks(lines: str | Iterable[str]) -> list[Task]:
    """Parse task text into a list of Task objects."""

    if isinstance(lines, str):
        source_lines = lines.splitlines()
    else:
        source_lines = list(lines)

    tasks: list[Task] = []
    for index, line in enumerate(source_lines, start=1):
        task = parse_task_line(line, line_number=index)
        if task is not None:
            tasks.append(task)
    return tasks


def _message(reason: str, raw_line: str, line_number: int | None) -> str:
    prefix = f"line {line_number}: " if line_number is not None else ""
    return f"{prefix}{reason}: {raw_line!r}"
