"""pyrob.utils"""

import os
import subprocess
import json
from pyrob.config import PIP, PROJECT_JSON, DEFAULT_SCRIPTS


def load_project_json() -> dict:
    """
    JSON can be an array, so raise if a dict not found
    """
    with open(PROJECT_JSON, "r", encoding="utf-8") as f:
        doc = json.load(f)

    if not isinstance(doc, dict):
        raise TypeError(f"{PROJECT_JSON} must be dict")

    return doc


def get_requirements() -> dict:
    """
    Cast pip freeze output to dict
    """
    req_bytes = subprocess.check_output([PIP, "freeze"])
    req_list = req_bytes.decode().splitlines()
    return dict([pkg.split("==") for pkg in req_list])


def generate_root() -> dict:
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


def generate_files(project_data: dict) -> None:
    """
    Create a /src dir with app entrypoint
    """
    src_path = os.path.join(os.getcwd(), "src")

    if not os.path.exists(src_path):
        os.makedirs(src_path)

    mod_doc_str = project_data["name"] if project_data["name"] else "A new project!"
    fn_doc_str = "Run the app with `pyrob run`"

    app_entrypoint = f"{src_path}/main.py"
    if not os.path.exists(app_entrypoint):
        with open(app_entrypoint, "x", encoding="utf-8") as main:
            main.write(f'"""\n{mod_doc_str}\n"""\n\n')
            main.write("def main():\n")
            main.write(f'    """\n    {fn_doc_str}\n    """\n')
            main.write('    print("Hello, World!")\n\n')
            main.write("main()\n")

    app_init = f"{src_path}/__init__.py"
    if not os.path.exists(app_init):
        with open(f"{src_path}/__init__.py", "x", encoding="utf-8"):
            pass

    fetch_gitignore()


def fetch_gitignore() -> None:
    """
    Fetch and save a gitignore template
    """
    os.system(
        " ".join(
            [
                "curl",
                "--silent",
                "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore",
                "> .gitignore",
            ]
        )
    )
