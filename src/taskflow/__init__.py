"""Taskflow demo package.

A deliberately small, functional Python project for demonstrating AICTX
repo-local continuity across coding-agent sessions.
"""

from .models import Task, TaskStatus
from .parser import parse_task_line, parse_tasks
from .summary import format_summary, summarize_tasks

__all__ = [
    "Task",
    "TaskStatus",
    "parse_task_line",
    "parse_tasks",
    "summarize_tasks",
    "format_summary",
]

__version__ = "0.1.0"
