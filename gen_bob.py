import json
from src.config import BOB_PATH

bob = {
    "name": "app_name",
    "version": "0.0.0",
    "scripts": {"hello": "echo 'Hello, World!'"},
    "requirements": {"PyYAML": "6.0.1"},
}

print(bob)

with open(BOB_PATH, "w+", encoding="utf-8") as file:
    json.dump(bob, file, indent=2)
