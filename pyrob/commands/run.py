"""
commands.run
"""

import os
import json
from pyrob.config import PROJECT_JSON, PYTHON, VENV_PATH


def run(args) -> None:
    """
    Look for a script in project.json and run it if found

    Runs src/main/py if no script given
    """
    script = args.script

    if not os.path.exists(".venv"):
        os.system(f"python3 -m venv {VENV_PATH}")

    if not script:
        os.system(f"{PYTHON} src/main.py")

    else:
        try:
            with open(PROJECT_JSON, "r", encoding="utf-8") as f:
                doc = json.load(f)

            if not isinstance(doc, dict):
                raise TypeError(f"{PROJECT_JSON} must be dict")

            scripts = doc["scripts"]

            if not isinstance(scripts, dict):
                raise TypeError(f"{PROJECT_JSON} scripts must be dict[str, str]")

            if script in doc["scripts"]:
                os.system(doc["scripts"][script])
            else:
                print(f'script "{script}" not found in {PROJECT_JSON}')

        except (json.decoder.JSONDecodeError, FileNotFoundError) as e:
            print(f"unable to run command -> {e}")
