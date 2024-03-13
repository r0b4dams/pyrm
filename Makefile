.PHONY: build install uninstall version clean upload_test

APP_NAME := pyrm
VENV := .venv
PY := $(VENV)/bin/python3
PIP := $(PY) -m pip
VERSION := $(shell cat VERSION)

dev: venv
	@echo "$(VENV) created. Run the following command to activate:"
	@echo "source $(VENV)/bin/activate" 

venv:
	@python3 -m venv $(VENV)
	@$(PIP) install --upgrade pip > /dev/null
	@chmod +x $(VENV)/bin/activate

lint: .venv
	@$(PIP) install --upgrade pylint > /dev/null
	@$(PY) -m pylint src 

format: .venv
	@$(PIP) install --upgrade black > /dev/null
	@$(PY) -m black src

test: .venv
	@$(PIP) install --upgrade pytest > /dev/null
	@$(PY) -m pytest tests -v

build: clean venv
	@$(PIP) install --upgrade build > /dev/null
	@$(PY) -m python3 -m build

install: build
	@$(PIP) install dist/$(APP_NAME)-$(VERSION).tar.gz

uninstall:
	@$(PIP) uninstall $(APP_NAME)

version:
	@echo $(v) | tr -d '\t' > VERSION

clean:
	@find . \
	\( -name .venv \
	-o -name dist \
	-o -name __pycache__ \
	-o -name "*.pytest_cache" \
	-o -name "*.egg-info" \
	\) -exec rm -rf {} +

upload_testpypi: build
	@$(PIP) install --upgrade twine
	@twine check dist/*
	@twine upload -r testpypi dist/*
	@twine upload dist/*