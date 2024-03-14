"""
pyrm.commands.install
"""

import os
import sys
from argparse import Namespace
from pyrm.utils import create_venv
from pyrm.config.vars import VENV, PROJECT_JSON


def install(args: Namespace) -> None:
    """
    Installs the given packages to the virtual environment

    Installs packages listed in project.json if no args given
    """

    # does .venv exist? if not need to create
    if not os.path.exists(VENV):
        create_venv()

    if len(args.pkgs) > 0:
        install_from_args(args.pkgs)
    else:
        install_from_meta()


def install_from_args(pkgs: list[str]) -> None:
    """
    TODO: doc str
    """
    args = " ".join(pkgs)
    print(args)

    # does project.json exist? if not create one
    if not os.path.exists(PROJECT_JSON):
        ...


def install_from_meta() -> None:
    """
    TODO: doc str
    """
    if not os.path.exists(VENV):
        sys.exit(f"Unable to install -> no args given and no {PROJECT_JSON} file found")
