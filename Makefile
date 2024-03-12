.PHONY: build install uninstall version clean upload_test

VENV := .venv
APP_NAME := pyrob
VERSION := $(shell cat VERSION)

venv:
	@python3 -m venv $(VENV)
	@chmod +x $(VENV)/bin/activate
	@echo "$(VENV) created. Run the following command to activate:"
	@echo "source $(VENV)/bin/activate" 

build: clean
	@python3 -m pip install --upgrade build
	@python3 -m build

install: build
	@python3 -m pip install dist/$(APP_NAME)-$(VERSION).tar.gz

uninstall:
	@python3 -m pip uninstall $(APP_NAME)

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
	@python3 -m pip install --upgrade twine
	@twine check dist/*
	@twine upload -r testpypi dist/*
	@twine upload dist/*