"""
commands.uninstall
"""

import os
import json
from argparse import Namespace
from config import PIP, VENV_PATH, PROJECT_JSON


def uninstall(args: Namespace) -> None:
    """
    uninstall the given package
    """
    try:
        if os.path.exists(VENV_PATH):
            packages = " ".join(list(args.packages))
            os.system(f"{PIP} uninstall -y {packages}")

        with open(PROJECT_JSON, "r", encoding="utf-8") as f:
            doc = json.load(f)

            if doc and doc["requirements"]:
                doc["requirements"] = {
                    pkg: ver
                    for pkg, ver in doc["requirements"].items()
                    if pkg not in args.packages
                }

        with open(PROJECT_JSON, "w+", encoding="utf-8") as f:
            json.dump(doc, f, indent=2)

    except (json.decoder.JSONDecodeError, FileNotFoundError) as e:
        print(e)
