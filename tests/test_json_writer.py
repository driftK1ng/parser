import pytest
import json
from JsonWriter import JsonWriter

@pytest.fixture
def temp_file(tmp_path):
    return tmp_path / "test_output.json"

def test_write_in_file(temp_file):
    writer = JsonWriter()

    test_data = [
        {
            'id': '1',
            'email':'test@test.com',
            'name': 'Test_name',
            'department': 'Test',
            'hours_worked': '2', 
            'rate': '3'
        }
    ]

    writer.write_in_file(test_data, temp_file)

    with open(temp_file, "r") as file:
        data = json.load(file)

    expected_data = {
        "Test": [
            {
                "name": "Test_name",
                "hours": '2',
                "payout": "$6",
                'rate': '3'
            }
        ]
    }

    assert data == expected_data

def test_write_in_file_1(temp_file):
    writer = JsonWriter()

    test_data = [
        {
            'id': '1',
            'email':'test@test.com',
            'name': 'Test_name',
            'department': 'Test',
            'hours_worked': '2', 
            'rate': '3'
        },
        {
            'id': '2',
            'email':'test@test_1.com',
            'name': 'Test_name_1',
            'department': 'New_Test',
            'hours_worked': '3', 
            'rate': '4'
        }
    ]

    writer.write_in_file(test_data, temp_file)

    with open(temp_file, "r") as file:
        data = json.load(file)

    expected_data = {
        "Test": [
            {
                "name": "Test_name",
                "hours": '2',
                "payout": "$6",
                'rate': '3'
            }
        ],
        "New_Test": [
            {
                "name": "Test_name_1",
                "hours": '3',
                "payout": "$12",
                'rate': '4'
            }
        ]
    }
    
def test_format_data():
    test_data = [
        {
            'id': '1',
            'email':'test@test.com',
            'name': 'Test_name',
            'department': 'Test',
            'hours_worked': '2', 
            'rate': '3'
        }
    ]
    writer = JsonWriter()

    expected_data = {
        'Test': [
            {
                "name": "Test_name",
                "rate": "3",
                "hours": '2',
                'payout': '$6'
            }
        ]
    }

    assert writer._format_data(test_data) == expected_data