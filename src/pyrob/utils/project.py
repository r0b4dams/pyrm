"""
pyrob.utils.project
"""

import os
import tempfile
import shutil
from .run import run


def make_venv(venv: str) -> None:
    """
    Create a virtual environment using the venv module

    Args:
        venv: path to virtual environment directory
    """
    run(["python3", "-m", "venv", venv])


def init(data: dict) -> None:
    """
    TODO: use a context manager and temp dir to setup project structure
    then copy everything to cwd
    """
    import pyrob
    from pyrob.utils import git, meta

    src = "".join([os.path.dirname(pyrob.__file__), "/", "__template__"])
    dst = os.getcwd()
    ignore = shutil.ignore_patterns("__pycache__*")

    with tempfile.TemporaryDirectory() as tmp:
        git.get_gitignore(tmp)
        meta.write(f"{tmp}/project.json", data)
        shutil.copytree(src, tmp, dirs_exist_ok=True, ignore=ignore)
        shutil.copytree(tmp, dst, dirs_exist_ok=True, ignore=ignore)
