import json


def read(filepath: str) -> dict:
    """
    Read json as dict
    """
    with open(filepath, encoding="utf-8") as f:
        doc = json.load(f)

    if isinstance(doc, dict):
        return doc

    raise TypeError(f"{filepath} must be a dict")


def write(filepath: str, data: dict) -> None:
    """
    Write dict to json
    """
    with open(filepath, "w+", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
