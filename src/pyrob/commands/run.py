"""
pyrob.commands.run
"""

import os
import sys
from pyrob.utils import meta, create_venv
from pyrob.config.vars import VENV, PROJECT_JSON


def run(args) -> None:
    """
    Runs the given script.
    The script must have a key of the same name in project.json.

    Args:
        args: Command line arguments from argparse

    Raises:
        SystemExit if no script given, virtual environment not found,
        or script not in project.json scripts
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
