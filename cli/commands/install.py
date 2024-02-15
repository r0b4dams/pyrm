"""
commands.install
"""

import os
import tempfile
import json
from argparse import Namespace
from utils import get_requirements
from config import PIP, PROJECT_JSON, VENV_PATH


def install(args: Namespace) -> None:
    """
    Calls pip to install the given package

    Installs packages listed in requirements if no package given
    """
    try:
        os.system(f"python3 -m venv {VENV_PATH}")

        if len(args.packages) > 0:
            install_from_args(args.packages)
        else:
            install_from_json()

    except json.decoder.JSONDecodeError as parse_err:
        print(f"unable to parse {PROJECT_JSON} -> {parse_err}")

    except (TypeError, AttributeError) as err:
        print(f"unable to install -> {err}")

    except KeyError:
        print(f"unable to install -> requirements not found in {PROJECT_JSON}")


def install_from_args(packages: list[str]) -> None:
    """
    Install given packages via pip

    Creates a project.json file if not found
    """
    doc = {}
    pkg_str = " ".join(list(packages))

    try:
        with open(PROJECT_JSON, "r", encoding="utf-8") as rf:
            doc = json.load(rf)

        if not isinstance(doc, dict):
            raise TypeError(f"{PROJECT_JSON} must be dict")

    except FileNotFoundError:
        pass

    os.system(f"{PIP} install {pkg_str}")
    doc["requirements"] = get_requirements()

    with open(PROJECT_JSON, "w+", encoding="utf-8") as wf:
        json.dump(doc, wf, indent=2)


def install_from_json() -> None:
    """
    Get dependency list from project.json and install
    """
    fd, tmp_req_path = tempfile.mkstemp()
    reqs_txt = ""

    try:
        with open(PROJECT_JSON, "r", encoding="utf-8") as f:
            doc = json.load(f)
            reqs = doc["requirements"]

        if not isinstance(doc, dict):
            raise TypeError(f"{PROJECT_JSON} must be dict")

        if not isinstance(reqs, dict):
            raise TypeError(f"{PROJECT_JSON} requirements must be dict[str, str]")

        reqs_txt = "\n".join(
            [f"{pkg}=={ver}" for pkg, ver in reqs.items() if isinstance(ver, str)]
        )

        with os.fdopen(fd, "w") as tmp:
            tmp.write(reqs_txt)
        os.system(f"{PIP} install -r {tmp_req_path}")

    except FileNotFoundError as fnf_err:
        print(f"unable to install -> {fnf_err}")

    finally:
        os.remove(tmp_req_path)
