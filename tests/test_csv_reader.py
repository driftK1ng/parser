import pytest
from config import fields, salary_fields
from CsvReader import CsvReader


@pytest.fixture
def temp_file(tmp_path):
    return tmp_path / "test_data.csv"


@pytest.fixture
def empty_file(tmp_path):
    return tmp_path / "empty_data.csv"

def test_read_file(temp_file, empty_file):
    reader = CsvReader()
    header = "id,email,name,department,hours_worked,hourly_rate\n"
    body = "1,test@test.com,Test_Name,Test,2,3\n"
    temp_file.write_text(header + body)
    empty_file.write_text("")
    data = reader.read_file([str(temp_file), 'test.txt', str(empty_file)])
    expected_data = [
        {"id": "1",
         "email": "test@test.com", 
         "name": "Test_Name", 
         "department": "Test", 
         "hours_worked": "2", 
         "rate": "3"}
    ]
    assert data == expected_data

def test_read_header():
    reader = CsvReader()
    header = "id,email,name,department,hours_worked,hourly_rate"
    reader._read_header(header)
    assert reader.placement == {"id": 0, "email": 1, "name": 2, "department": 3, "hours_worked": 4, "rate": 5}
    reader = CsvReader()
    header = "id,email,name,department,hours_worked,rate"
    reader._read_header(header)
    assert reader.placement == {"id": 0, "email": 1, "name": 2, "department": 3, "hours_worked": 4, "rate": 5}

def test_read_header_err():
    reader = CsvReader()
    header = "id,email,name,department,hours_worked,hourly_rate\n"
    reader._read_header(header)
    assert reader.placement == {"id": 0, "email": 1, "name": 2, "department": 3, "hours_worked": 4}

def test_read_body():
    reader = CsvReader()
    header = "id,email,name,department,hours_worked,hourly_rate"
    reader._read_header(header)
    body = "1,test@test.com,Test_Name,Test,2,3"
    expected_data = { "id": "1", 
         "email": "test@test.com",
         "name": "Test_Name",
         "department": "Test",
         "hours_worked": "2",
         "rate": "3"}
    
    assert reader._read_body(body) == expected_data

def test_set_placement():
    reader = CsvReader()
    title = "id"
    index = 1
    reader._set_placement(title, index)
    assert reader.placement["id"] == 1
    title = "name"
    index = 2
    reader._set_placement(title, index)
    assert reader.placement['name'] == 2

def test_clear_placement():
    reader = CsvReader()
    title = "id"
    index = 1
    reader._set_placement(title, index)
    reader._clear_placement()
    assert reader.placement == {"id": 1}

def test_clear_empty_placement():
    reader = CsvReader()
    reader._clear_placement()
    assert reader.placement == {}
