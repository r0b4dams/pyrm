"""
pyrm.commands.init
"""

import os
from argparse import Namespace
from pyrm.utils import meta, get_git_config
from pyrm.config.vars import PROJECT_JSON


def init(args: Namespace) -> None:
    """
    TODO: doc str
    """
    try:
        defaults = from_default()
        data = defaults if args.y else from_prompts(defaults)
        meta.write(PROJECT_JSON, data)
    except (KeyboardInterrupt, EOFError):
        print("\nexit init")


def from_default() -> dict:
    """
    TODO: doc str
    """
    user, email = get_git_config()
    *_, current_folder_name = os.path.split(os.getcwd())

    return {
        "name": current_folder_name,
        "version": "0.0.1",
        "author": f"{user} <{email}>",
        "description": "A new project!",
        "scripts": {"foo": "echo foo bar baz"},
    }


def from_prompts(defaults: dict) -> dict:
    """
    TODO: doc str
    """
    data = {**defaults}
    ignore = {"repository", "scripts"}

    for key, value in defaults.items():
        if key in ignore:
            continue

        if r := input(f"{key} ({value}): "):
            data[key] = r

    return data
