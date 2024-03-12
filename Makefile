.PHONY: build install uninstall version clean upload_test

APP_NAME := pyrob
VENV := .venv
PY := $(VENV)/bin/python3
PIP := $(VENV)/bin/pip
VERSION := $(shell cat VERSION)

dev: venv
	@echo "$(VENV) created. Run the following command to activate:"
	@echo "source $(VENV)/bin/activate" 

venv:
	@python3 -m venv $(VENV)
	@chmod +x $(VENV)/bin/activate

lint: venv
	@$(PIP) install --upgrade pylint > /dev/null
	@pylint src 

format: venv
	@$(PIP) install --upgrade black > /dev/null
	@black src

test: venv
	@$(PIP) install --upgrade pytest > /dev/null
	@pytest tests -v

build: clean venv
	@$(PIP) install --upgrade build > /dev/null
	@python3 -m build

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
	-o -name "*.egg-info" \
	\) -exec rm -rf {} +

upload_test: build
	@$(PIP) install --upgrade twine
	@twine check dist/*
	@twine upload -r testpypi dist/*
	@twine upload dist/*