from __future__ import annotations

from taskflow.models import Task, TaskStatus
from taskflow.parser import parse_tasks
from taskflow.summary import format_summary, summarize_tasks


def test_summarize_tasks_counts_supported_statuses() -> None:
    tasks = [
        Task(TaskStatus.TODO, "record demo"),
        Task(TaskStatus.TODO, "publish repo"),
        Task(TaskStatus.DONE, "write tests"),
    ]

    assert summarize_tasks(tasks) == {
        "todo": 2,
        "done": 1,
        "total": 3,
    }


def test_summarize_empty_tasks() -> None:
    assert summarize_tasks([]) == {
        "todo": 0,
        "done": 0,
        "total": 0,
    }


def test_format_summary_is_stable() -> None:
    assert format_summary({"todo": 2, "done": 1, "total": 3}) == "todo: 2\ndone: 1\ntotal: 3"


def test_parse_and_summarize_integration() -> None:
    tasks = parse_tasks(
        """
        TODO: create demo repo
        TODO: record session one
        DONE: add pytest coverage
        """
    )

    assert format_summary(summarize_tasks(tasks)) == "todo: 2\ndone: 1\ntotal: 3"
