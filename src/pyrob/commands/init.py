"""
pyrob.commands.init
"""

import os
import shutil
from argparse import Namespace
import pyrob
from pyrob.utils import meta, git, create_venv
from pyrob.commands.install import install_from_args
from pyrob.config.vars import PROJECT_JSON, VENV


def init(args: Namespace) -> None:
    """
    Initialize a new project and generate a project.json file.

    Args:
        args: Command line arguments from argparse
    """
    try:
        base = from_default()
        data = base if args.y else with_prompts(base)

        shutil.copytree(
            src="".join([os.path.dirname(pyrob.__file__), "/", "__template__"]),
            dst=os.getcwd(),
            dirs_exist_ok=True,
            ignore=shutil.ignore_patterns("__pycache__*"),
        )

        meta.write(PROJECT_JSON, data)
        print("Creating virtual environment...")
        create_venv(VENV)
        print("Installing packages...")
        install_from_args(["black", "pylint", "mypy", "pytest"])
        print("Project initialized! Happy hacking!")

    except (KeyboardInterrupt, EOFError):
        print("\nexit init")


def from_default() -> dict:
    """
    Generate a base dict to serve as project.json shape.

    Returns:
        dict with default project.json values
    """
    user, email = git.get_config()
    _, current_folder_name = os.path.split(os.getcwd())

    return {
        "name": current_folder_name,
        "version": "0.0.1",
        "author": f"{user} <{email}>",
        "description": "A new project!",
        "scripts": {
            "lint": "pylint src",
            "test": "pytest tests -v",
            "typecheck": "mypy src",
            "format": "black src",
        },
    }


def with_prompts(default: dict) -> dict:
    """
    Prompt user to override default project metadata

    Args:
        default: a base dict with default values.

    Returns:
        dict with values set to user input
    """
    data = {**default}
    ignore = {"repository", "scripts"}

    for key, value in data.items():
        if key in ignore:
            continue

        if r := input(f"{key} ({value}): "):
            data[key] = r

    return data
