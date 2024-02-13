#!/usr/bin/python3

"""
doc str
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
    cmd_install.add_argument("package", type=str, default=None)
    cmd_install.set_defaults(func=commands.install)

    # parse the args and call whatever function was selected
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
