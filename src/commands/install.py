"""install"""

import os
from utils import create_requirements, save_requirements
from config import PIP, REQS_PATH, VENV_PATH
from .clean import clean


def install(args):
    """
    Calls pip to install the given package

    Installs all packages if no package given
    """
    clean()
    os.system(f"python3 -m venv {VENV_PATH}")

    if not os.path.exists(REQS_PATH):
        create_requirements()

    if args.package is not None:
        os.system(f"{PIP} install {args.package}")
        save_requirements()
    else:
        os.system(f"{PIP} install -r {REQS_PATH}")
