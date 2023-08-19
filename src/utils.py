import json
import datetime


def load_file(path):
    """
    Функция для загрузки json-файла.
    :param path: путь до файла
    :return: list
    """
    with open(path, "r", encoding="UTF-8") as f:
        operations = json.load(f)
        return operations


def get_executed(operations):
    """
    Функция фильтрует по статусу операции.
    :param operations: список словарей
    :return:list
    """
    result = []
    for operation in operations:
        if 'state' in operation and operation['state'] == 'EXECUTED':
            result.append(operation)
    return result

def get_sorted_by_date(operations):
    """
    Функция сортирует по дате.
    :param operations:
    :return:list
    """
    result = sorted(operations,
           key=lambda operation: datetime.datetime.fromisoformat(operation.get('date')),
           reverse=True)
    return result

def get_five_operations(operations):
    """
    Функция возвращает последние  5 успешных операций
    :param operations:
    :return: list
    """
    return operations[:5]


def formate_date(datetime):
    """
    Функция преобразует даты к виду ДД.ММ.ГГГГ.
    :param datetime:
    :return: str
    """
    only_date = datetime[:10]
    date_splitted = only_date.split('-')
    return '.'.join(reversed(date_splitted))

def hide_requisites(requisites):
    """
    Функция маскирует номер счета/карты.
    :param requisites:
    :return: str
    """
    req_info = requisites.split()
    number = req_info[-1]
    if requisites.lower().startswith("счет"):
        hided_number = f"**{number[-4:]}"
    else:
        hided_number = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
    req_info[-1] = hided_number
    return ' '.join(req_info)


def prepare_to_output(operation):
    """
    Функция возвращает всю информацию об опреации.
    :param operation:
    :return: list
    """
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
