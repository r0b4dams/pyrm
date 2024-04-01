"""
pyrob.commands.init
"""

import os
import argparse
from pyrob.utils import project, pip, git
from pyrob.config.vars import VENV
from .install import install_from_args


def init(args: argparse.Namespace) -> None:
    """
    Initialize a new project and generate a project.json file.

    Args:
        args: Command line arguments from argparse
    """
    try:
        print("Initializing project...")

        base = from_default()
        data = base if args.y else with_prompts(base)

        git.init()
        project.make_venv(VENV)
        project.init(data)
        install_from_args("black", "pylint", "mypy", "pytest")

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
