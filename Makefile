.PHONY: dev venv lint format typecheck test build install uninstall version clean upload_testpypi release

APP_NAME := pyrob
VERSION := $(shell python3 -c "from src import $(APP_NAME); print($(APP_NAME).__version__)")

VENV := .venv
PY := $(VENV)/bin/python3
PIP := $(PY) -m pip

dev: venv
	@echo "$(APP_NAME) $(VERSION)"
	@echo "$(VENV) created. Run the following command to activate:"
	@echo "source $(VENV)/bin/activate" 

venv:
	@python3 -m venv $(VENV)
	@$(PIP) install --upgrade pip build black mypy pylint pytest
	@chmod +x $(VENV)/bin/activate

lint: .venv
	@$(PY) -m pylint src --ignore-paths src/pyrm/__templates__

format: .venv
	@$(PY) -m black src

typecheck: .venv
	@$(PY) -m mypy src

test: .venv
	@$(PY) -m pytest tests -v

build: clean venv
	@$(PY) -m build

install: build
	@python3 -m pip install dist/$(APP_NAME)-$(VERSION).tar.gz

uninstall:
	@python3 -m pip uninstall -y $(APP_NAME)

clean:
	@scripts/clear_tags
	@find . \
	\( -name .venv \
	-o -name dist \
	-o -name __pycache__ \
	-o -name "*.mypy_cache" \
	-o -name "*.pytest_cache" \
	-o -name "*.egg-info" \
	\) -exec rm -rf {} +

release:
	@chmod +x scripts/release
	@scripts/release