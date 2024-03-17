"""
pyrob.commands.init
"""

import os
from argparse import Namespace
from pyrob.utils import meta, git
from pyrob.config.vars import PROJECT_JSON


def init(args: Namespace) -> None:
    """
    Initialize a new project and generate a project.json file.

    Args:
        args: Command line arguments from argparse
    """
    try:
        base = from_default()
        data = base if args.y else with_prompts(base)
        meta.write(PROJECT_JSON, data)

    except (KeyboardInterrupt, EOFError):
        print("\nexit init")


def from_default() -> dict:
    """
    Generate a base dict to serve as project.json shape.

    Returns:
        dict with default project.json values
    """
    user, email = git.get_config()
    *_, current_folder_name = os.path.split(os.getcwd())

    return {
        "name": current_folder_name,
        "version": "0.0.1",
        "author": f"{user} <{email}>",
        "description": "A new project!",
        "scripts": {"foo": "echo foo bar baz"},
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
