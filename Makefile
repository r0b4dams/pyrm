.PHONY: build install uninstall

APP_NAME := "pyrob"
VERSION := $(shell cat $(APP_NAME)/__init__.py | grep __version__ | cut -d "=" -f 2 | xargs echo -n)

# requires build to use setuptools
# pip install --upgrade build 
build: clean
	@python3 -m build

install: build
	@pip install dist/$(APP_NAME)-$(VERSION).tar.gz

uninstall:
	@pip uninstall $(APP_NAME)

clean:
	@rm -rf dist pyrob.egg-info
	@find . \( -name __pycache__ -o -name "*.pyc" \) -delete