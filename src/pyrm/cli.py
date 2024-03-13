"""
TODO: doc string
"""

from argparse import ArgumentParser
from . import __version__


def main():
    """
    TODO: doc string
    """
    parser = ArgumentParser(
        prog="pyrm", description="A CLI to manage dependencies in a Python project"
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s {__version__}"
    )

    subparsers = parser.add_subparsers()

    args = parser.parse_args()
