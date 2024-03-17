"""
pyrob.utils.git
"""

from . import run


def get_config() -> tuple[str, str]:
    """
    Get username and email from git config.

    Returns:
        tuple with username and email
    """
    user = run(["git", "config", "user.name"])
    email = run(["git", "config", "user.email"])
    return user, email
