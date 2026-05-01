from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class TaskStatus(StrEnum):
    """Supported task states in the demo baseline.

    Parser edge cases remain intentionally out of scope for this session.
    """

    TODO = "TODO"
    DONE = "DONE"
    BLOCKED = "BLOCKED"


@dataclass(frozen=True, slots=True)
class Task:
    status: TaskStatus
    title: str

    def as_line(self) -> str:
        return f"{self.status.value}: {self.title}"
