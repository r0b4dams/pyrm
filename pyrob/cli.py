#!/usr/bin/python3

"""
A simple CLI to manage dependencies in a Python project
"""

import argparse
import pyrob.commands
import pyrob.config


def main():
    parser = argparse.ArgumentParser(
        prog="pyrob", description="A CLI to manage dependencies in a Python project"
    )
    subparsers = parser.add_subparsers()

    cmd_init = subparsers.add_parser("init")
    cmd_init.add_argument("-y", default=False, action="store_true")
    cmd_init.set_defaults(func=pyrob.commands.init)

    cmd_run = subparsers.add_parser("run")
    cmd_run.add_argument("script", action="store", default=None, nargs="?")
    cmd_run.set_defaults(func=pyrob.commands.run)

    cmd_add = subparsers.add_parser("install")
    cmd_add.add_argument("packages", nargs="*", default=None)
    cmd_add.set_defaults(func=pyrob.commands.install)

    cmd_remove = subparsers.add_parser("uninstall")
    cmd_remove.add_argument("packages", nargs="+")
    cmd_remove.set_defaults(func=pyrob.commands.uninstall)

    cmd_clean = subparsers.add_parser("clean")
    cmd_clean.set_defaults(func=pyrob.commands.clean)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        print(f"{__name__} v{pyrob.config.VERSION}")
