from os import getenv
from importlib.metadata import version

VERSION = version("pyrob") or getenv("VERSION", "0.0.0")
VENV_PATH = ".venv"
PYTHON = f"{VENV_PATH}/bin/python3"
PIP = f"{VENV_PATH}/bin/pip"
PROJECT_JSON = "project.json"
DEFAULT_SCRIPTS = {"foo": "echo foo bar baz"}
