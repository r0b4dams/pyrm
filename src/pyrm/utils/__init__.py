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


def pip_install(*pkgs: str) -> dict:
    run(["python3", "-m", "pip", *pkgs])
    return get_reqs(as_dict=True)


def get_reqs(as_dict: bool = True) -> str:
    """
    Get packages installed to virtual environment

    Returns a str of package==version pairs separated by newlines
    """
    output = run(["python3", "-m", "pip", "freeze"])
    return dict([pkg.split("==") for pkg in output.splitlines()]) if as_dict else output


def get_git_config() -> tuple[str, str]:
    """
    Returns a tuple of the username and email from git config
    """
    user = run(["git", "config", "user.name"])
    email = run(["git", "config", "user.email"])
    return user, email
