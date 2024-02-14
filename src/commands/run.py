"""
commands.run
"""

import os
import json
from config import PROJECT_JSON


def run(args) -> None:
    """
    Look for a script in project.json and run it if found
    """
    (script,) = args.script

    try:
        with open(PROJECT_JSON, "r", encoding="utf-8") as f:
            doc = json.load(f)
            if script in doc["scripts"] and script is not None:
                os.system(doc["scripts"][script])
            else:
                print(f'script "{script}" not found in {PROJECT_JSON} requirements')

    except (json.decoder.JSONDecodeError, FileNotFoundError) as e:
        print(e)
