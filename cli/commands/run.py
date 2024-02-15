"""
commands.run
"""

import os
import json
from config import PROJECT_JSON


def run(args) -> None:
    """
    Look for a script in project.json and run it if found

    Runs src/main/py if no script given
    """
    script = args.script

    if not script:
        os.system("python3 src/main.py")

    else:
        try:
            with open(PROJECT_JSON, "r", encoding="utf-8") as f:
                doc = json.load(f)

                if doc["scripts"] and script in doc["scripts"]:
                    os.system(doc["scripts"][script])
                else:
                    print(f'script "{script}" not found in {PROJECT_JSON}')

        except (json.decoder.JSONDecodeError, FileNotFoundError) as e:
            print(f"unable to run command -> {e}")
