"""
pyrob.utils.git
"""

import os
from pyrob.config.vars import GITIGNORE_URL
from . import run


def init() -> None:
    """
    Initialize git repository if not exists
    """
    if not os.path.exists(".git"):
        run(["git", "init"])


def get_config() -> tuple[str, str]:
    """
    Get username and email from git config.

    Returns:
        tuple with username and email
    """
    user = run(["git", "config", "user.name"])
    email = run(["git", "config", "user.email"])
    return user, email


def get_gitignore() -> None:
    os.system(" ".join(["curl", "--silent", GITIGNORE_URL, ">", ".gitignore"]))
