import pytest
import requests

from datetime import date, datetime

from models.user import UserModel
from models.client import ClientModel
from models.schedule import ScheduleModel


# test user
def test_post_user():
    response = requests.post(
        "http://localhost:5000/api/user",
        data={
            "id":666,
            "first_name": "teste",
            "last_name": "teste",
            "email": "jdfsklj@nxncx",
            "password": "sjdfjljslfdsj"
            })
    assert response.status_code == 201

def test_get_user():
    response = requests.get("http://localhost:5000/api/user")
    assert response.status_code == 200

def test_put_user():
    response = requests.put(
        "http://localhost:5000/api/user/1",
        data={
            "first_name": "testado",
            "email": "jdfsklj@nxncx"
            })
    assert response.status_code == 204



# test client
def test_post_client():
    response = requests.post("http://localhost:5000/api/client",
        data={
            "id":666,
            "first_name": "teste",
            "last_name": "teste",
            "cpf": "69328462",
            "rg_number": "654987362",
            "rg_uf": "sp",
            "email": "hdjfs@djflks",
            "phone": "11964658699"
            })
    assert response.status_code == 201

def test_get_client():
    response = requests.get("http://localhost:5000/api/client")
    assert response.status_code == 200

def test_put_client():
    response = requests.put("http://localhost:5000/api/client/1",
        data={
            "first_name": "testado",
            "email": "hdjfs@djflkshahahahhaha"
            })
    assert response.status_code == 204



# test schedule
def test_post_schedule():
    response = requests.post("http://localhost:5000/api/schedule",
        data = {
            "id":666,
            "status": 64365983294,
            "created_at": 76,
            "client_id": 1,
            "date": "26/03/2020",
            "time": "11:00",
            "vehicle_board": "ABC-6666",
            "vehicle_brand": "CHEVROLET",
            "vehicle_model": "CELTA",
            "vehicle_year": "2001"
            })
    assert response.status_code == 201

def test_get_schedule():
    response = requests.get("http://localhost:5000/api/schedule")
    assert response.status_code == 200

def test_put_schedule():
    response = requests.put(f"http://localhost:5000/api/schedule/1",
        data={
            "status": 12345
            })
    assert response.status_code == 204


# test report
def test_post_report():
    response = requests.post("http://localhost:5000/api/report",
        data = {
            "status": 8,
            "vehicle_id": 1,
            "client_id": 1,
            "description": "bla bla bla"
            })
    assert response.status_code == 201

def test_get_report():
    response = requests.get("http://localhost:5000/api/report")
    assert response.status_code == 200

def test_put_report():
    response = requests.put(f"http://localhost:5000/api/report/1",
        data={
            "status": 5
            })
    assert response.status_code == 204


# test destroy
def test_destroy():
    try:
        user_response = requests.delete(f"http://localhost:5000/api/user/1")
        client_response = requests.delete(f"http://localhost:5000/api/client/1")
        schedule_response = requests.delete(f"http://localhost:5000/api/schedule/1")
        report_response = requests.delete(f"http://localhost:5000/api/report/1")
    except Exception as e:
        print(e)


    assert user_response.status_code == 204
    assert client_response.status_code == 204
    assert schedule_response.status_code == 204
    assert report_response.status_code == 204
