"""
pyrm.utils.meta
"""

import sys
import json


def read(file: str) -> dict:
    """
    TODO: doc str
    """
    try:
        with open(file, "r", encoding="utf-8") as f:
            doc = json.load(f)

            if not isinstance(doc, dict):
                raise TypeError(f"{file} must be dict. Received {type(doc)}")

            return doc

    except (json.decoder.JSONDecodeError, TypeError) as e:
        sys.exit(str(e))


def write(file: str, data: dict) -> None:
    """
    TODO: doc str
    """
    with open(file, "w+", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
