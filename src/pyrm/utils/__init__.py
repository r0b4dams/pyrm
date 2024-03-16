"""
pyrm.utils
"""

import subprocess
from ..config.vars import PYTHON


def run(cmd: list[str]) -> str:
    """
    TODO: doc str
    """
    return subprocess.check_output(cmd).decode().strip()


def create_venv(venv: str) -> None:
    """
    TODO: doc str
    """
    run(["python3", "-m", "venv", venv])


def pip_install(*pkgs: str) -> dict:
    """
    TODO: doc str
    """
    print(run([PYTHON, "-m", "pip", "install", *pkgs]))
    return get_reqs()


def get_reqs() -> dict:
    """
    TODO: doc str
    """
    requirements = run([PYTHON, "-m", "pip", "freeze"])
    return dict([pkg.split("==") for pkg in requirements.splitlines() if "==" in pkg])


def get_git_config() -> tuple[str, str]:
    """
    TODO: doc str
    """
    user = run(["git", "config", "user.name"])
    email = run(["git", "config", "user.email"])
    return user, email
