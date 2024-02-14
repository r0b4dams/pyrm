"""
commands.install
"""

import os
import subprocess
import tempfile
import json
from argparse import Namespace
from config import PIP, PROJECT_JSON, VENV_PATH


def install(args: Namespace) -> None:
    """
    Calls pip to install the given package

    Installs packages listed in requirements if no package given
    """
    os.system(f"python3 -m venv {VENV_PATH}")

    if len(args.packages) > 0:
        install_from_args(args.packages)
    else:
        install_from_json()


def install_from_args(packages: list[str]) -> None:
    """
    Install given packages via pip

    Creates a bob.yaml file if not found
    """
    packages = " ".join(list(packages))
    os.system(f"{PIP} install {packages}")

    req_bytes = subprocess.check_output([PIP, "freeze"])
    req_list = req_bytes.decode().splitlines()
    requirements = dict([pkg.split("==") for pkg in req_list])

    try:
        with open(PROJECT_JSON, "r", encoding="utf-8") as f:
            doc = json.load(f)
            doc["requirements"] = requirements

        with open(PROJECT_JSON, "w", encoding="utf-8") as f:
            json.dump(doc, f, sort_keys=False, indent=2)

    except FileNotFoundError:
        with open(PROJECT_JSON, "w+", encoding="utf-8") as f:
            json.dump({"requirements": requirements}, f, indent=2)


def install_from_json() -> None:
    """
    Get dependency list from bob.json and install
    """
    fd, tmp_req_path = tempfile.mkstemp()
    reqs = ""

    try:
        with open(PROJECT_JSON, "r", encoding="utf-8") as f:
            doc = json.load(f)
            deps = doc["requirements"]
            reqs = "\n".join([f"{pkg}=={ver}" for pkg, ver in deps.items()])

    except FileNotFoundError:
        print(f"unable to install: {PROJECT_JSON} not found")

    except (KeyError, AttributeError):
        print("unable to install: requirements not found")

    else:
        with os.fdopen(fd, "w") as tmp:
            tmp.write(reqs)
        os.system(f"{PIP} install -r {tmp_req_path}")

    finally:
        os.remove(tmp_req_path)
