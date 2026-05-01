from __future__ import annotations

import pytest

from taskflow.models import TaskStatus
from taskflow.parser import TaskParseError, parse_task_line, parse_tasks


def test_parse_todo_line() -> None:
    task = parse_task_line("TODO: write quickstart")

    assert task is not None
    assert task.status == TaskStatus.TODO
    assert task.title == "write quickstart"


def test_parse_done_line() -> None:
    task = parse_task_line("DONE: add tests")

    assert task is not None
    assert task.status == TaskStatus.DONE
    assert task.title == "add tests"


def test_parse_is_case_insensitive_for_supported_statuses() -> None:
    task = parse_task_line("todo: trim lowercase input")

    assert task is not None
    assert task.status == TaskStatus.TODO
    assert task.title == "trim lowercase input"


def test_parse_ignores_blank_lines_and_comments() -> None:
    assert parse_task_line("") is None
    assert parse_task_line("   ") is None
    assert parse_task_line("# comment") is None


def test_parse_tasks_multiple_lines() -> None:
    tasks = parse_tasks(
        """
        # release checklist
        TODO: record demo
        DONE: write README
        """
    )

    assert [task.as_line() for task in tasks] == [
        "TODO: record demo",
        "DONE: write README",
    ]


def test_parse_requires_separator() -> None:
    with pytest.raises(TaskParseError, match="missing ':' separator"):
        parse_task_line("TODO write quickstart", line_number=3)


def test_parse_requires_title() -> None:
    with pytest.raises(TaskParseError, match="task title cannot be empty"):
        parse_task_line("TODO:", line_number=4)


def test_parse_blocked_line() -> None:
    task = parse_task_line("BLOCKED: waiting for API")

    assert task is not None
    assert task.status == TaskStatus.BLOCKED
    assert task.title == "waiting for API"


def test_parse_blocked_line_is_case_insensitive_and_trims_whitespace() -> None:
    task = parse_task_line("  blocked : waiting for API  ")

    assert task is not None
    assert task.status == TaskStatus.BLOCKED
    assert task.title == "waiting for API"


def test_parse_unsupported_status_lists_blocked_in_allowed_values() -> None:
    with pytest.raises(
        TaskParseError,
        match="unsupported task status 'WAITING' \\(expected: TODO, DONE, BLOCKED\\)",
    ):
        parse_task_line("waiting: on API", line_number=7)
