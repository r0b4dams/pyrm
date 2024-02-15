"""
commands.init
"""

import os
import json
from argparse import Namespace
from typing import Tuple
from config import PROJECT_JSON, DEFAULT_SCRIPTS


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
            print("Aborted")
            return

    except (KeyboardInterrupt, EOFError):
        print("\nexit init")

    else:
        with open(PROJECT_JSON, "w+", encoding="utf-8") as f:
            json.dump(project_data, f, indent=2)

        generate_entrypoint(project_data)


def generate_entrypoint(project_data: dict):
    """
    Create a source folder with app entrypoint
    """
    src_path = os.path.join(os.getcwd(), "src")

    if not os.path.exists(src_path):
        os.makedirs(src_path)

    mod_doc_str = project_data["name"] if project_data["name"] else "A new project!"
    fn_doc_str = "Run the app with `pyrob run`"
    with open(f"{src_path}/main.py", "w+", encoding="utf-8") as main:
        main.write(f'"""\n{mod_doc_str}\n"""\n\n')
        main.write("def main():\n")
        main.write(f'    """\n    {fn_doc_str}\n    """\n')
        main.write('    print("Hello, World!")\n\n')
        main.write("main()\n")


def generate_root():
    """
    Setup a dict to create a project.json file
    """
    *_, current_folder_name = os.path.split(os.getcwd())

    root = {
        "name": current_folder_name,
        "version": "0.0.1",
        "author": "bob",  # get from git?
        "description": "a new project",
        "scripts": DEFAULT_SCRIPTS,
    }

    return root


def defaults() -> Tuple[dict, dict]:
    """
    Create a dict with some default data
    """
    data = None
    root = generate_root()

    try:
        with open(PROJECT_JSON, "r", encoding="utf-8") as f:
            doc = json.load(f)

        if not isinstance(doc, dict):
            raise TypeError(f"{PROJECT_JSON} must be dict")

        data = {**root}  # preserve order of root keys

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
