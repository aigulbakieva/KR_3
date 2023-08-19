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


def formate_date(datetime):
    only_date = datetime[:10]
    date_splitted = only_date.split('-')
    return '.'.join(reversed(date_splitted))

def hide_requisites(requisites):
    req_info = requisites.split()
    number = req_info[-1]
    if requisites.lower().startswith("счет"):
        hided_number = f"**{number[-4:]}"
    else:
        hided_number = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
    req_info[-1] = hided_number
    return ' '.join(req_info)


def prepare_to_output(operation):
    # line_1 processing
    line_1_elements = []
    date = operation['date']
    line_1_elements.append(formate_date(date))
    line_1_elements.append(operation['description'])
    line_1 = ' '.join(line_1_elements)

    # line_2 processing
    line_2_elements = []
    if operation.get('from'):
        from_info = hide_requisites(operation.get('from'))
        line_2_elements.append(from_info)
    else:
        line_2_elements.append("Наличный взнос")
    line_2_elements.append("->")
    to_info = hide_requisites(operation.get('to'))
    line_2_elements.append(to_info)
    line_2 = ' '.join(line_2_elements)

    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']
    line_3 = f"{amount} {currency}"

    return (f"{line_1}\n"
            f"{line_2}\n"
            f"{line_3}")
