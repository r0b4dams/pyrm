"""
commands.install
"""

import os
from utils import create_reqs, save_reqs
from config import PIP, REQS_PATH, VENV_PATH


def install(args):
    """
    Calls pip to install the given package

    Installs packages listed in requirements if no package given
    """
    os.system(f"python3 -m venv {VENV_PATH}")

    if not os.path.exists(REQS_PATH):
        create_reqs()

    if len(args.package) > 0:
        packages = " ".join([pkg for pkg in args.package])
        os.system(f"{PIP} install {packages}")
    else:
        os.system(f"{PIP} install -r {REQS_PATH}")

    save_reqs()
