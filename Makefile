PYTHON ?= python3
VENV ?= .venv
VENV_PYTHON := $(VENV)/bin/python
VENV_PIP := $(VENV_PYTHON) -m pip
VENV_READY := $(VENV)/.taskflow-ready
INSTALL_INPUTS := pyproject.toml Makefile $(shell find src tests -type f | sort)

.PHONY: check-python venv install test test-no-install run demo-target clean ci codex-last-session codex-usage-report codex-usage-report-json

check-python:
	@$(PYTHON) -c 'import sys; raise SystemExit(0 if sys.version_info >= (3, 11) else 1)' || { echo "taskflow demo requires Python >= 3.11. Run with: make test PYTHON=python3.12"; exit 1; }

$(VENV_PYTHON): | check-python
	@if [ ! -x "$(VENV_PYTHON)" ]; then $(PYTHON) -m venv $(VENV); fi

$(VENV_READY): $(VENV_PYTHON) $(INSTALL_INPUTS)
	$(VENV_PIP) install --upgrade pip
	$(VENV_PIP) install --ignore-installed -e '.[dev]'
	@touch $(VENV_READY)

venv: $(VENV_READY)

install: $(VENV_READY)

test: check-python $(VENV_READY)
	$(VENV_PYTHON) -m pytest -q

test-no-install:
	$(PYTHON) -m pytest -q

run: check-python $(VENV_READY)
	$(VENV_PYTHON) -m taskflow.cli examples/tasks.txt

demo-target: check-python $(VENV_READY)
	$(VENV_PYTHON) -m taskflow.cli examples/session_1_target.txt

ci: test run demo-target

clean:
	rm -rf .pytest_cache build dist *.egg-info src/*.egg-info src/taskflow/__pycache__ tests/__pycache__



codex-last-session:
	@$(PYTHON) scripts/codex_usage_report.py --json | $(PYTHON) -c 'import json,sys; print(json.load(sys.stdin)["session_file"])'

codex-usage-report:
	@$(PYTHON) scripts/codex_usage_report.py

codex-usage-report-json:
	@$(PYTHON) scripts/codex_usage_report.py --json
