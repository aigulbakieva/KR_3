import json
import datetime


def load_file():
    with open("operations.json", "r", encoding="UTF-8") as f:
        operations = json.load(f)
        return operations


def get_executed(operations):
    result = []
    for operation in operations:
        if 'state' in operation and operation['state'] == 'EXECUTED':
            result.append(operation)
    return result

