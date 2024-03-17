"""
pyrob.utils.pip
"""

from . import run
from ..config.vars import PYTHON


def install_from_reqs(path: str) -> None:
    """
    Install packages to virtual environment from a requirements file.

    Args:
        path: path to requirements file
    """
    run([PYTHON, "-m", "pip", "install", "-r", path])


def install_from_args(*pkgs: str) -> None:
    """
    Install given sequence of packages to virtual environment.

    Args:
        pkgs: sequence of packages to uninstall
    """
    run([PYTHON, "-m", "pip", "install", *pkgs])


def uninstall(*pkgs: str) -> None:
    """
    Uninstall given sequence of packages from virtual environment.

    Args:
        pkgs: sequence of packages to uninstall
    """
    run([PYTHON, "-m", "pip", "uninstall", "-y", *pkgs])


def requirements() -> dict:
    """
    Cast pip freeze result to dict for package.json.

    Returns:
        A dict containing packages and their versions
    """
    reqs = run([PYTHON, "-m", "pip", "freeze"])
    return dict([pkg.split("==") for pkg in reqs.splitlines() if "==" in pkg])
