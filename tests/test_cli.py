from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def test_cli_reads_file(tmp_path: Path) -> None:
    task_file = tmp_path / "tasks.txt"
    task_file.write_text("TODO: record demo\nDONE: add tests\n", encoding="utf-8")

    result = subprocess.run(
        [sys.executable, "-m", "taskflow.cli", str(task_file)],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert result.stdout.strip() == "todo: 1\ndone: 1\ntotal: 2"
    assert result.stderr == ""


def test_cli_reports_parse_errors(tmp_path: Path) -> None:
    task_file = tmp_path / "tasks.txt"
    task_file.write_text("BLOCKED: waiting for API\n", encoding="utf-8")

    result = subprocess.run(
        [sys.executable, "-m", "taskflow.cli", str(task_file)],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 2
    assert "unsupported task status 'BLOCKED'" in result.stderr
