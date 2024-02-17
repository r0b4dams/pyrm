.PHONY: build install uninstall

APP_NAME := "pyrob"
VERSION := $(shell cat VERSION)

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