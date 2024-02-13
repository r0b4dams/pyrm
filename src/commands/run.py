"""
commands.run
"""

import os
import yaml


def run(args):
    """
    look for a script and run it if found
    """
    (script,) = args.script

    with open("bob.yaml", "r", encoding="utf-8") as file:
        meta = yaml.safe_load(file)

        if script in meta["scripts"]:
            os.system(meta["scripts"][script])
        else:
            print("script not found")
