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

def get_sorted_by_date(operations):
    result = sorted(operations,
           key=lambda operation: datetime.datetime.fromisoformat(operation.get('date')),
           reverse=True)
    return result

def get_five_operations(operations):
    return operations[:5]
