"""
pyrob.commands.clean
"""

import os
import shutil

dirs_to_remove = [".venv", "__pycache__"]


def clean(_) -> None:
    """
    Remove cache artifacts
    """
    for dirpath, dirnames, _ in os.walk("."):
        for dirname in dirnames:
            if dirname in dirs_to_remove:
                shutil.rmtree(os.path.join(dirpath, dirname))
