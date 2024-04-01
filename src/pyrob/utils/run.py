"""
pyrob.utils.run
"""

import subprocess


def run(cmd: list[str]) -> str:
    """
    Run the given command

    Returns:
        stdout from subprocess
    """
    return subprocess.check_output(cmd).decode().strip()
