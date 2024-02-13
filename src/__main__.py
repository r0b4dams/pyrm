#!/usr/bin/python3

"""
A simple CLI to manage dependencies in a Python project
"""
import argparse
import commands

parser = argparse.ArgumentParser(prog="pybob", description="Python dev environment CLI")
subparsers = parser.add_subparsers(required=True)

# commands

cmd_start = subparsers.add_parser("start")


cmd_add = subparsers.add_parser("install")
cmd_add.add_argument("package", nargs="*", default=None)
cmd_add.set_defaults(func=commands.install)


cmd_remove = subparsers.add_parser("uninstall")
cmd_remove.add_argument("package", nargs="+")
cmd_remove.set_defaults(func=commands.uninstall)


cmd_clean = subparsers.add_parser("clean")
cmd_clean.set_defaults(func=commands.clean)

args = parser.parse_args()
args.func(args)
