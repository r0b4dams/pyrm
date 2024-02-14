"""
commands.install
"""

import os
import subprocess
import tempfile
import json
from argparse import Namespace
from config import PIP, PROJECT_JSON, VENV_PATH

# if no args:
# look for package.json
# exit if not found
# get reqs from package.json
# exit if parse err or not found

# if args
#


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

    except AttributeError as attr_err:
        print(f"unable to install -> {attr_err}")

    except KeyError:
        print(f"unable to install: requirements not found in {PROJECT_JSON}")


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
        with open(PROJECT_JSON, "r", encoding="utf-8") as r:
            doc = json.load(r)
            doc["requirements"] = requirements

        with open(PROJECT_JSON, "w", encoding="utf-8") as w:
            json.dump(doc, w, sort_keys=False, indent=2)

    # create a new project.json file if not found
    except FileNotFoundError:
        with open(PROJECT_JSON, "w+", encoding="utf-8") as f:
            json.dump({"requirements": requirements}, f, indent=2)


def install_from_json() -> None:
    """
    Get dependency list from project.json and install
    """
    fd, tmp_req_path = tempfile.mkstemp()
    reqs_txt = ""

    try:
        with open(PROJECT_JSON, "r", encoding="utf-8") as f:
            doc = json.load(f)
            deps = doc["requirements"]

            if not isinstance(deps, dict):
                raise AttributeError("requirements must be dict[str, str]")

            reqs_txt = "\n".join(
                # ignores ver values that ane not strings
                [f"{pkg}=={ver}" for pkg, ver in deps.items() if isinstance(ver, str)]
            )

    except FileNotFoundError as fnf_err:
        print(f"unable to install -> {fnf_err}")

    else:
        with os.fdopen(fd, "w") as tmp:
            tmp.write(reqs_txt)

        os.system(f"{PIP} install -r {tmp_req_path}")

    finally:
        os.remove(tmp_req_path)
