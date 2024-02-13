"""utils.create_requirements"""

from config import REQS_PATH


def create_requirements():
    """
    write a requirements file
    https://pip.pypa.io/en/stable/reference/requirements-file-format/
    """
    with open(REQS_PATH, "w", encoding="utf-8") as f:
        f.write("# Install packages with `pybob install <pkg_name>`")
