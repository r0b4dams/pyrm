.PHONY: build install uninstall version clean upload_testpypi

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
	@$(PIP) install --upgrade pip > /dev/null
	@chmod +x $(VENV)/bin/activate

lint: .venv
	@$(PIP) install --upgrade pylint > /dev/null
	@$(PY) -m pylint src --ignore-paths src/pyrm/__templates__

format: .venv
	@$(PIP) install --upgrade black > /dev/null
	@$(PY) -m black src

typecheck: .venv
	@$(PIP) install --upgrade mypy > /dev/null
	@$(PY) -m mypy src

test: .venv
	@$(PIP) install --upgrade pytest > /dev/null
	@$(PY) -m pytest tests -v

build: clean venv
	@$(PIP) install --upgrade build > /dev/null
	@$(PY) -m build

install: build
	@python3 -m pip install dist/$(APP_NAME)-$(VERSION).tar.gz

uninstall:
	@python3 -m pip uninstall -y $(APP_NAME)

clean:
	@find . \
	\( -name .venv \
	-o -name dist \
	-o -name __pycache__ \
	-o -name "*.mypy_cache" \
	-o -name "*.pytest_cache" \
	-o -name "*.egg-info" \
	\) -exec rm -rf {} +

# Note: add #HOME/.pypirc to skip auth prompt
# https://packaging.python.org/en/latest/guides/using-testpypi/#setting-up-testpypi-in-pypirc
upload_testpypi: build
	@$(PIP) install --upgrade twine
	@twine check dist/*
	@twine upload -r testpypi dist/*
	@twine upload dist/*

install_from_testpypi: .venv
	@$(PIP) install -i https://test.pypi.org/simple/ $(APP_NAME)

install_from_testpypi_global:
	@pip install -i https://test.pypi.org/simple/ $(APP_NAME)