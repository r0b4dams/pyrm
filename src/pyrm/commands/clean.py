"""pyrob.commands.clean"""

import os
import shutil
from pyrm.config import VENV_PATH


def clean(*_) -> None:
    """remove artifacts"""
    clean_caches()
    clean_venv()


def clean_caches() -> None:
    """remove __pycache__ dirs"""
    for path, *_ in os.walk(os.getcwd(), topdown=True):
        if path.endswith("__pycache__"):
            shutil.rmtree(path)


def clean_venv() -> None:
    """remove virtual environment"""
    venv_path = os.path.join(os.getcwd(), VENV_PATH)
    if os.path.exists(venv_path):
        shutil.rmtree(venv_path)
