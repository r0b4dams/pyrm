"""
commands.uninstall
"""

import os
from utils import save_reqs
from config import PIP


def uninstall(args):
    """
    uninstall the given package
    """
    packages = " ".join(list(args.package))
    os.system(f"{PIP} uninstall -y {packages}")
    save_reqs()
