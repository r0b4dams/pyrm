"""utils"""

import subprocess
from config import PIP


def get_requirements() -> dict:
    """Cast pip freeze output to dict"""
    req_bytes = subprocess.check_output([PIP, "freeze"])
    req_list = req_bytes.decode().splitlines()
    return dict([pkg.split("==") for pkg in req_list])
