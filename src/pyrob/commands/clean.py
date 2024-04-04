"""
pyrob.commands.clean
"""

from pyrob.utils.run import run


def clean():
    """
    Remove cache artifacts:

    """
    run(["ls"])
