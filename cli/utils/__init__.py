"""utils"""

import os
import subprocess
from config import PIP, DEFAULT_SCRIPTS


def get_requirements() -> dict:
    """Cast pip freeze output to dict"""
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


def generate_entrypoint(project_data: dict) -> None:
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
