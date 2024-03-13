"""
pyrm.cli
"""

from argparse import ArgumentParser
from . import __version__


def main():
    """
    entrypoint
    """
    parser = ArgumentParser(
        prog="pyrm", description="A CLI to manage dependencies in a Python project"
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s {__version__}"
    )

    parser.parse_args()
