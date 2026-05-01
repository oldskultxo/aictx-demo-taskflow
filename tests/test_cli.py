from __future__ import annotations

import subprocess
import sys
import os
from pathlib import Path


def _cli_env() -> dict[str, str]:
    env = os.environ.copy()
    src_path = str(Path(__file__).resolve().parents[1] / "src")
    existing = env.get("PYTHONPATH")
    env["PYTHONPATH"] = src_path if not existing else f"{src_path}{os.pathsep}{existing}"
    return env


def test_cli_reads_file(tmp_path: Path) -> None:
    task_file = tmp_path / "tasks.txt"
    task_file.write_text("TODO: record demo\nDONE: add tests\nBLOCKED: waiting for API\n", encoding="utf-8")

    result = subprocess.run(
        [sys.executable, "-m", "taskflow.cli", str(task_file)],
        capture_output=True,
        text=True,
        check=False,
        env=_cli_env(),
    )

    assert result.returncode == 0
    assert result.stdout.strip() == "todo: 1\ndone: 1\nblocked: 1\ntotal: 3"
    assert result.stderr == ""


def test_cli_stdin_reads_blocked_tasks(tmp_path: Path) -> None:
    task_file = tmp_path / "tasks.txt"
    task_file.write_text("BLOCKED: waiting for API\nDONE: add tests\n", encoding="utf-8")

    result = subprocess.run(
        [sys.executable, "-m", "taskflow.cli", str(task_file)],
        capture_output=True,
        text=True,
        check=False,
        env=_cli_env(),
    )

    assert result.returncode == 0
    assert result.stdout.strip() == "todo: 0\ndone: 1\nblocked: 1\ntotal: 2"
    assert result.stderr == ""


def test_cli_reads_utf8_bom_prefixed_file(tmp_path: Path) -> None:
    task_file = tmp_path / "tasks.txt"
    task_file.write_text("\ufeffTODO: record demo\nBLOCKED: waiting for API\nDONE: add tests\n", encoding="utf-8")

    result = subprocess.run(
        [sys.executable, "-m", "taskflow.cli", str(task_file)],
        capture_output=True,
        text=True,
        check=False,
        env=_cli_env(),
    )

    assert result.returncode == 0
    assert result.stdout.strip() == "todo: 1\ndone: 1\nblocked: 1\ntotal: 3"
    assert result.stderr == ""
