"""
pyrm.commands.run
"""

import os
import sys
from pyrm.utils import meta, create_venv
from pyrm.config.vars import VENV, PROJECT_JSON


def run(args) -> None:
    """
    TODO: doc str
    """
    if not args.script:
        sys.exit("No script given")

    if not os.path.exists(VENV):
        create_venv(VENV)

    try:
        script = meta.read(PROJECT_JSON)["scripts"][args.script]
        os.system(script)
    except (FileNotFoundError, KeyError, TypeError) as e:
        sys.exit(f"Unable to run command -> {e}")
