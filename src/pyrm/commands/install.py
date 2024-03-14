"""
pyrm.commands.install
"""

import os
import sys
import tempfile
from argparse import Namespace
from pyrm.utils import meta, run, create_venv, pip_install
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
    doc = {}

    try:
        doc = meta.read(PROJECT_JSON)
    except FileNotFoundError:
        pass

    doc["requirements"] = pip_install(*pkgs)

    meta.write(PROJECT_JSON, doc)


def install_from_meta() -> None:
    """
    TODO: doc str
    """
    fd, tmp_req_path = tempfile.mkstemp()

    try:
        doc = meta.read(PROJECT_JSON)
        reqs = doc["requirements"]

        if not isinstance(reqs, dict):
            raise TypeError(f"{PROJECT_JSON} requirements must be dict[str, str]")

        # cast dict to str of package==version pairs separated by newlines
        # same format as returned by 'pip freeze'
        reqs_txt = "\n".join([f"{pkg}=={ver}" for pkg, ver in reqs.items()])

        with os.fdopen(fd, "w") as tmp:
            tmp.write(reqs_txt)

        run(["pip", "install", "-r", tmp_req_path])

    except (KeyError, TypeError) as e:
        sys.exit(f"unable to install -> {e}")

    finally:
        os.remove(tmp_req_path)
