from __future__ import annotations

from collections import Counter
from collections.abc import Iterable

from .models import Task, TaskStatus


def summarize_tasks(tasks: Iterable[Task]) -> dict[str, int]:
    """Return counts for every supported status."""

    counter = Counter(task.status for task in tasks)
    return {
        "todo": counter[TaskStatus.TODO],
        "done": counter[TaskStatus.DONE],
        "blocked": counter[TaskStatus.BLOCKED],
        "total": sum(counter.values()),
    }


def format_summary(summary: dict[str, int]) -> str:
    """Format a summary dict as stable CLI-friendly text."""

    return "\n".join(
        [
            f"todo: {int(summary.get('todo', 0))}",
            f"done: {int(summary.get('done', 0))}",
            f"blocked: {int(summary.get('blocked', 0))}",
            f"total: {int(summary.get('total', 0))}",
        ]
    )
