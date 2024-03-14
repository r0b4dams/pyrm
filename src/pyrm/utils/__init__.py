"""
pyrm.utils
"""

import subprocess


def run(cmd: list[str]) -> str:
    """
    Helper to run a shell command

    Returns stdout of command
    """
    return subprocess.check_output(cmd).decode().strip()


def create_venv() -> None:
    """
    Create a virtual environment
    """
    run(["python3", "-m", "venv", ".venv"])


def get_reqs() -> str:
    """
    Get packages installed to virtual environment

    Returns a str of package==version pairs separated by newlines
    """
    return run(["python3", "-m", "pip", "freeze"])


def get_reqs_dict() -> dict:
    """
    Returns a dict created from a requirements str
    """
    return dict([pkg.split("==") for pkg in get_reqs().splitlines()])


def get_git_config() -> tuple[str, str]:
    """
    Returns a tuple of the username and email from git config
    """
    user = run(["git", "config", "user.name"])
    email = run(["git", "config", "user.email"])
    return user, email
