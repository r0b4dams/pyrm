#!/usr/bin/python3

"""
A simple CLI to manage dependencies in a Python project
"""
import argparse
import commands


def main():
    """CLI entrypoint"""

    parser = argparse.ArgumentParser(
        prog="pybob", description="Python dev environment CLI"
    )
    subparsers = parser.add_subparsers(required=True)

    # commands

    # install
    cmd_install = subparsers.add_parser("install")
    cmd_install.add_argument(
        "package",
        nargs="?",
        default=None,
    )
    cmd_install.set_defaults(func=commands.install)

    # clean
    cmd_clean = subparsers.add_parser("clean")
    cmd_clean.set_defaults(func=commands.clean)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
