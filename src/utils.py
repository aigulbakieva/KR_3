import json


def load_file():
    with open("operations.json", "r", encoding="UTF-8") as f:
        operations = json.load(f)
        return operations
