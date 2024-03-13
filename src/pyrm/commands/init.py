"""pyrob.commands.init"""

import json
from argparse import Namespace
from typing import Tuple
from pyrm.config import PROJECT_JSON
from pyrm.utils import load_project_json, generate_base, generate_files


def init(args: Namespace) -> None:
    """
    Create project files
    """
    try:
        if args.y:
            project_data, *_ = defaults()
            print("Project initialized with:")
            print(json.dumps(project_data, indent=2))
        else:
            project_data = prompts()
            print("Initializing project with:")
            print(json.dumps(project_data, indent=2))

            if not args.y and input("Is this OK? (yes) "):
                print("Abort init")  # quit if anything other than empty str
                return

    except (KeyboardInterrupt, EOFError):
        print("\nexit init")

    else:
        with open(PROJECT_JSON, "w+", encoding="utf-8") as f:
            json.dump(project_data, f, indent=2)

        generate_files(project_data)


def defaults() -> Tuple[dict, dict]:
    """
    Create a dict with some default data

    If a project.json file exists, attempts to grab data from it
    """
    base = generate_base()
    data = {**base}

    try:
        doc = load_project_json()

        for k, v in doc.items():
            if k in base and not v:
                data[k] = base[k]
            else:
                data[k] = v

    except FileNotFoundError:
        pass

    except (json.decoder.JSONDecodeError, TypeError) as e:
        print(f"{PROJECT_JSON} found but unable to parse -> {e}")
        print("using defaults")

    return data, base


def prompts() -> dict:
    """
    Get project data from user input
    """
    data, base = defaults()

    if not data:
        data = base

    for key in base:
        if key == "scripts":
            continue
        res = input(f"{key} ({data[key]}): ")
        if res:
            data[key] = res

    return data
