"""
pyrm.commands.run
"""

import os
import sys
from pyrm.utils import meta, create_venv
from pyrm.config.vars import VENV, PROJECT_JSON


def run(args) -> None:
    """
    Run the given command if it exists in project.json
    """
    if not args.script:
        sys.exit("no script given")

    if not os.path.exists(VENV):
        create_venv()

    try:
        script = meta.read(PROJECT_JSON)["scripts"][args.script]
        os.system(script)
    except (FileNotFoundError, KeyError, TypeError) as e:
        sys.exit(f"unable to run command -> {e}")
