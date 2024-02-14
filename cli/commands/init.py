"""
commands.init
"""

import os
import sys
import json
from argparse import Namespace
from typing import Tuple
from config import PROJECT_JSON, DEFAULT_SCRIPTS


def init(args: Namespace) -> None:
    """
    Initialize a project and add a project.json file containing project data
    """
    project_data = defaults() if args.y else prompts()

    if "scripts" not in project_data:
        project_data["scripts"] = DEFAULT_SCRIPTS

    with open(PROJECT_JSON, "w+", encoding="utf-8") as f:
        json.dump(project_data, f, indent=2)

    # TODO create a src folder if not exists


def defaults() -> Tuple[dict, dict]:
    """
    Create a dict with some default data
    """
    *_, current_folder_name = os.path.split(os.getcwd())

    data = None
    root = {
        "name": current_folder_name,
        "version": "0.0.1",
        "author": "bob",  # get from git?
        "description": "a new project",
    }

    try:
        with open(PROJECT_JSON, "r+", encoding="utf-8") as f:
            doc: dict[str, str] = json.load(f)
        if doc:
            data = {**root}
            for k, v in doc.items():
                str_not_empty = isinstance(v, str) and not v.strip()
                if k in root and str_not_empty:
                    data[k] = root[k]

    except (json.decoder.JSONDecodeError, FileNotFoundError):
        pass

    return data, root


def prompts() -> dict:
    """
    Get project data from user input
    """
    data, root = defaults()

    if not data:
        data = root

    try:
        for key in root:
            res = input(f"{key} ({data[key]}): ")
            if res:
                data[key] = res

    except (KeyboardInterrupt, EOFError):
        print()
        sys.exit()

    else:
        return data
