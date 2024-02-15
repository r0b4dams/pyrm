"""
commands.init
"""

import os
import json
from argparse import Namespace
from typing import Tuple
from utils import generate_root, generate_entrypoint
from config import PROJECT_JSON


def init(args: Namespace) -> None:
    """
    Initialize a project and add a project.json file containing project data
    """
    try:
        if args.y:
            project_data, *_ = defaults()
        else:
            project_data = prompts()

        print("Initializing project with:")
        print(json.dumps(project_data, indent=2))

        if not args.y and input("Is this OK? (yes) "):
            print("Abort mission")  # quit if anything other than empty str
            return

    except (KeyboardInterrupt, EOFError):
        print("\nexit init")

    else:
        with open(PROJECT_JSON, "w+", encoding="utf-8") as f:
            json.dump(project_data, f, indent=2)
        generate_entrypoint(project_data)

        os.system(
            "curl https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore >> .gitignore &> /dev/null"
        )


def defaults() -> Tuple[dict, dict]:
    """
    Create a dict with some default data
    """
    root = generate_root()
    data = {**root}

    try:
        with open(PROJECT_JSON, "r", encoding="utf-8") as f:
            doc = json.load(f)

        if not isinstance(doc, dict):
            raise TypeError(f"{PROJECT_JSON} must be dict")

        # for the root keys,
        # if value falsy go with root value
        # else put back k/v found in doc as-is
        for k, v in doc.items():
            v_is_empty_str = isinstance(v, str) and not v.strip()
            if k in root and v_is_empty_str:
                data[k] = root[k]
            else:
                data[k] = v

    except FileNotFoundError:
        pass

    except (json.decoder.JSONDecodeError, TypeError) as e:
        print(f"{PROJECT_JSON} found but unable to parse -> {e}")
        print("using defaults")

    return data, root


def prompts() -> dict:
    """
    Get project data from user input
    """
    data, root = defaults()

    if not data:
        data = root

    for key in root:
        if key == "scripts":
            continue
        res = input(f"{key} ({data[key]}): ")
        if res:
            data[key] = res

    return data
