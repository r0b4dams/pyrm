#!/usr/bin/python3

"""
A simple CLI to manage dependencies in a Python project
"""
import argparse
import commands

parser = argparse.ArgumentParser(prog="bob", description="Python dev environment CLI")


# commands
subparsers = parser.add_subparsers()

cmd_run = subparsers.add_parser("run")
cmd_run.add_argument("script", nargs=1)
cmd_run.set_defaults(func=commands.run)

cmd_add = subparsers.add_parser("install")
cmd_add.add_argument("package", nargs="*", default=None)
cmd_add.set_defaults(func=commands.install)

cmd_remove = subparsers.add_parser("uninstall")
cmd_remove.add_argument("package", nargs="+")
cmd_remove.set_defaults(func=commands.uninstall)

cmd_clean = subparsers.add_parser("clean")
cmd_clean.set_defaults(func=commands.clean)

args = parser.parse_args()

if hasattr(args, "func"):
    args.func(args)
else:
    print("run init")
