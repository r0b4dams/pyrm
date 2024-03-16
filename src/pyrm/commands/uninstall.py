"""pyrob.commands.uninstall"""

import os
import sys
import json
from argparse import Namespace
from pyrm.utils import meta, run, get_reqs
from pyrm.config.vars import PYTHON, VENV, PROJECT_JSON


def uninstall(args: Namespace) -> None:
    """
    Uninstalls the given packages from the virtual environment
    """

    if not os.path.exists(VENV):
        sys.exit(f"{VENV} not found")

    try:
        doc = meta.read(PROJECT_JSON)
    except FileNotFoundError:
        sys.exit(f"{PROJECT_JSON} not found")

    run([PYTHON, "-m", "pip", "uninstall", "-y", *args.pkgs])
    doc["requirements"] = get_reqs()

    with open(PROJECT_JSON, "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2)
