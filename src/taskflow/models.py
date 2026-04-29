from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class TaskStatus(StrEnum):
    """Supported task states in the demo baseline.

    BLOCKED is intentionally not supported in v0.1.0. That makes a clear,
    safe coding-agent demo task: add BLOCKED support in session 1, then let
    AICTX help session 2 resume from the saved context.
    """

    TODO = "TODO"
    DONE = "DONE"


@dataclass(frozen=True, slots=True)
class Task:
    status: TaskStatus
    title: str

    def as_line(self) -> str:
        return f"{self.status.value}: {self.title}"
