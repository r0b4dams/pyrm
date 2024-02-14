#!/usr/bin/python3

"""
A simple CLI to manage dependencies in a Python project
"""

import argparse
import commands


def main():
    parser = argparse.ArgumentParser(
        prog="bob", description="Python dev environment CLI"
    )
    subparsers = parser.add_subparsers()

    # commands

    cmd_init = subparsers.add_parser("init")
    cmd_init.add_argument("-y", type=bool, default=False)
    cmd_init.set_defaults(func=commands.init)

    cmd_run = subparsers.add_parser("run")
    cmd_run.add_argument("script", nargs=1)
    cmd_run.set_defaults(func=commands.run)

    cmd_add = subparsers.add_parser("install")
    cmd_add.add_argument("packages", nargs="*", default=None)
    cmd_add.set_defaults(func=commands.install)

    cmd_remove = subparsers.add_parser("uninstall")
    cmd_remove.add_argument("packages", nargs="+")
    cmd_remove.set_defaults(func=commands.uninstall)

    cmd_clean = subparsers.add_parser("clean")
    cmd_clean.set_defaults(func=commands.clean)

    args = parser.parse_args()
    args.func(args)

    # if hasattr(args, "func"):


if __name__ == "__main__":
    main()
