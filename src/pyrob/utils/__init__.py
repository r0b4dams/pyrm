"""
pyrob.utils
"""

import subprocess


def run(cmd: list[str]) -> str:
    """
    Run the given command

    Returns:
        stdout from subprocess
    """
    return subprocess.check_output(cmd).decode().strip()


def create_venv(venv: str) -> None:
    """
    Create a virtual environment using the venv module

    Args:
        venv: path to virtual environment directory
    """
    run(["python3", "-m", "venv", venv])
