"""utils.save_reqs"""

import os
from config import PIP, REQS_PATH


def save_reqs():
    """
    dump saved venv packages to requirements file
    """
    if os.path.exists(REQS_PATH):
        os.system(f"{PIP} freeze > {REQS_PATH}")
