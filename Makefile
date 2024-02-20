.PHONY: build clean install uninstall clean

APP_NAME := pyrob
VERSION := $(shell cat VERSION)

all:
	@echo $(APP_NAME) v$(VERSION)

build: clean
	@python3 -m pip install --upgrade build
	@python3 -m build

install: build
	@pip install dist/$(APP_NAME)-$(VERSION).tar.gz

uninstall:
	@pip uninstall $(APP_NAME)

version:
	@echo $(v) | tr -d '\t' > VERSION

clean:
	@find . \
	\( -name .venv \
	-o -name dist \
	-o -name __pycache__ \
	-o -name "*.egg-info" \
	\) -exec rm -rf {} +