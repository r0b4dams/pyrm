"""install"""

import os

from config import PIP, REQS_PATH, VENV_PATH
from utils import create_requirements, save_requirements


def install(args):
    """
    Calls pip to install the given package

    Installs all packages if no package given
    """
    os.system(f"python3 -m venv {VENV_PATH}")

    if not os.path.exists(REQS_PATH):
        create_requirements()

    if args.package is not None:
        os.system(f"{PIP} install {args.package}")
        save_requirements()
    else:
        os.system(f"{PIP} install -f {REQS_PATH}")
