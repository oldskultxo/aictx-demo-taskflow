from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .parser import TaskParseError, parse_tasks
from .summary import format_summary, summarize_tasks


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="taskflow",
        description="Summarize simple TODO/DONE task files.",
    )
    parser.add_argument(
        "path",
        nargs="?",
        help="Task file to read. If omitted, reads from standard input.",
    )
    return parser


def read_input(path: str | None) -> str:
    if not path:
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        tasks = parse_tasks(read_input(args.path))
    except (OSError, TaskParseError) as exc:
        parser.exit(2, f"taskflow: error: {exc}\n")

    print(format_summary(summarize_tasks(tasks)))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
