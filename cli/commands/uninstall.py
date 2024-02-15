"""
commands.uninstall
"""

import os
import json
from argparse import Namespace
from config import PIP, VENV_PATH, PROJECT_JSON
from utils import get_requirements


def uninstall(args: Namespace) -> None:
    """
    Calls pip to uninstall the given package
    """
    if not os.path.exists(VENV_PATH):
        print(f"unable to uninstall: {VENV_PATH} not found")
        return

    try:
        with open(PROJECT_JSON, "r", encoding="utf-8") as f:
            doc = json.load(f)

        if not isinstance(doc, dict):
            raise TypeError(f"{PROJECT_JSON} must be dict")

        packages = " ".join(list(args.packages))
        os.system(f"{PIP} uninstall -y {packages}")
        doc["requirements"] = get_requirements()

        with open(PROJECT_JSON, "w+", encoding="utf-8") as f:
            json.dump(doc, f, indent=2)

    except (json.decoder.JSONDecodeError, FileNotFoundError) as e:
        print(f"unable to parse {PROJECT_JSON}: {e}")

    except TypeError as type_err:
        print(f"unable to uninstall -> {type_err}")
