"""
pyrm.cli
"""

from argparse import ArgumentParser
from pyrm import __version__, commands


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

    # commands

    subparsers = parser.add_subparsers()

    init = subparsers.add_parser("init")
    init.add_argument("-y", default=False, action="store_true")
    init.set_defaults(func=commands.init)

    install = subparsers.add_parser("install")
    install.add_argument("pkgs", nargs="*", default=None)
    install.set_defaults(func=commands.install)

    parser.parse_args()
    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
