"""
pyrm init
- prompt for info to write to project.json

pyrm init -y
- skip prompts 
"""

import os
from argparse import Namespace


def init(args: Namespace) -> None:
    try:
        if args.y:
            print(from_default())
        else:
            print(from_prompts())

    except (KeyboardInterrupt, EOFError):
        print("\nexit init")


def from_default() -> dict:
    *_, current_folder_name = os.path.split(os.getcwd())
    return {
        "name": current_folder_name,
        "version": "0.0.1",
        "author": "",
        "description": "A new project!",
        "scripts": {"foo": "echo foo bar baz"},
    }


def from_prompts():
    ignore = {"scripts"}
    data = from_default()

    for key, value in data.items():
        if key in ignore:
            continue

        if r := input(f"{key} ({value}):"):
            data[key] = r

    return data
