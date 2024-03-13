"""pyrob.cli"""

from argparse import ArgumentParser
from pyrm import commands
from pyrm.config import VERSION


def main():
    """entrypoint"""
    parser = ArgumentParser(
        prog="pyrob", description="A CLI to manage dependencies in a Python project"
    )
    subparsers = parser.add_subparsers()

    # commands

    init = subparsers.add_parser("init")
    init.add_argument("-y", default=False, action="store_true")
    init.set_defaults(func=commands.init)

    run = subparsers.add_parser("run")
    run.add_argument("script", action="store", default=None, nargs="?")
    run.set_defaults(func=commands.run)

    install = subparsers.add_parser("install")
    install.add_argument("packages", nargs="*", default=None)
    install.set_defaults(func=commands.install)

    uninstall = subparsers.add_parser("uninstall")
    uninstall.add_argument("packages", nargs="+")
    uninstall.set_defaults(func=commands.uninstall)

    clean = subparsers.add_parser("clean")
    clean.set_defaults(func=commands.clean)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)

    # no command entered
    else:
        print(__name__, f"{VERSION}")
