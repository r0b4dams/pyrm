"""
utils.project
"""

import json


def read_json(filepath: str) -> dict:
    """
    Cast json to dict
    """
    with open(filepath, encoding="utf-8") as f:
        doc = json.load(f)

    if isinstance(doc, dict):
        return doc

    raise TypeError(f"{filepath} must be a dict")


def write_json(_path: str, _doc: dict) -> None:
    """
    TODO: write dict to project.json
    """
