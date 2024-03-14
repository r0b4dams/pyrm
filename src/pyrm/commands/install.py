"""
pyrm.commands.install
"""

import os
import sys
from argparse import Namespace
from pyrm.utils import meta, create_venv, pip_install
from pyrm.config.vars import VENV, PROJECT_JSON


def install(args: Namespace) -> None:
    """
    Installs the given packages to the virtual environment

    Installs packages listed in project.json if no args given
    """

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
    requirements = pip_install(*pkgs)

    if doc := meta.read(PROJECT_JSON):
        doc["requirements"] = requirements
        meta.write(PROJECT_JSON, doc)
    else:
        meta.write(PROJECT_JSON, {"requirements": requirements})


def install_from_meta() -> None:
    """
    TODO: doc str
    """
    if not os.path.exists(PROJECT_JSON):
        sys.exit(f"Unable to install -> no args given and no {PROJECT_JSON} file found")
