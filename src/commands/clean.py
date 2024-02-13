"""
commands.clean
"""

import os
import shutil
from config import VENV_PATH


def clean(*_):
    """remove virtual environment and __pycache__ dirs"""
    clean_caches()
    clean_venv()


def clean_caches():
    """remove __pycache__ dirs"""
    for path, *_ in os.walk(os.getcwd(), topdown=True):
        if path.endswith("__pycache__"):
            shutil.rmtree(path)


def clean_venv():
    """remove virtual environment"""
    venv_path = os.path.join(os.getcwd(), VENV_PATH)
    if os.path.exists(venv_path):
        shutil.rmtree(venv_path)
