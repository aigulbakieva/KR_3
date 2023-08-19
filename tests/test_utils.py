import pytest
from src.utils import (load_file, get_executed, get_sorted_by_date, get_five_operations,
                       formate_date, hide_requisites, prepare_to_output)
import os
from config import ROOT_DIR


def test_load_file():
    test_data_file_path = os.path.join(ROOT_DIR, 'tests', 'data_for_test.json')
    assert load_file(test_data_file_path) == [1, 2, 3]


def test_get_executed():
    data = [
        {
            'state': 'EXECUTED'
        },
        {
            'state': 'CANCELED'
        },
        {
            'state': 'EXECUTED'
        }
    ]

    expected = [
        {
            'state': 'EXECUTED'
        },
        {
            'state': 'EXECUTED'
        }
    ]
    assert get_executed(data) == expected


def test_get_sorted():
    data = [
        {
            'date': "2019-08-16T04:23:41.621065"
        },
        {
            'date': "2018-08-16T04:23:41.621065"
        },
        {
            'date': "2019-04-16T04:23:41.621065"
        }
    ]
    expected = [
        {
            'date': "2019-08-16T04:23:41.621065"
        },
        {
            'date': "2019-04-16T04:23:41.621065"
        },
        {
            'date': "2018-08-16T04:23:41.621065"
        }
    ]
    assert get_sorted_by_date(data) == expected


def test_get_five():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected = [1, 2, 3, 4, 5]
    assert get_five_operations(data) == expected


def test_formate_date():
    date = "2019-08-16T04:23:41.621065"
    expected = "16.08.2019"
    assert formate_date(date) == expected


@pytest.mark.parametrize('bill, expected', [
    ("Счет 46878338893256147528", "Счет **7528"),
    ("Visa Platinum 3530191547567121", "Visa Platinum 3530 19** **** 7121"),
    ("MasterCard 8826230888662405", "MasterCard 8826 23** **** 2405")
])
def test_hide_requisites(bill, expected):
    assert hide_requisites(bill) == expected


def test_prepare_from_bill_to_bill():
    data = {
        "id": 200634844,
        "state": "EXECUTED",
        "date": "2018-02-13T04:43:11.374324",
        "operationAmount": {
            "amount": "42210.20",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 33355011456314142963",
        "to": "Счет 45735917297559088682"
    }
    expected = (f"13.02.2018 Перевод организации\n"
                f"Счет **2963 -> Счет **8682\n"
                f"42210.20 руб.")
    assert prepare_to_output(data) == expected

def test_prepare_cash_to_bill():
    data = {
        "id": 200634844,
        "state": "EXECUTED",
        "date": "2018-02-13T04:43:11.374324",
        "operationAmount": {
            "amount": "42210.20",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие счета",
        "to": "Счет 45735917297559088682"
    }
    expected = (f"13.02.2018 Открытие счета\n"
                f"Наличный взнос -> Счет **8682\n"
                f"42210.20 руб.")
    assert prepare_to_output(data) == expected
