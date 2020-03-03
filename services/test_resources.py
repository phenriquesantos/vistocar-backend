import pytest
import requests

from datetime import date

from models.user import UserModel
from models.client import ClientModel
from models.phone import PhoneModel
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
            "password": "kjdslksjl"
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
        data={
            "id":666,
            "status": 64365983294,
            "created_at": 76,
            "client_id": 1,
            "last_update": 87
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


# test destroy
def test_destroy():
    user = UserModel.get_by_id(1)
    client = ClientModel.get_by_email("hdjfs@djflkshahahahhaha")
    schedule = ScheduleModel.get_by_status(12345)

    user.delete()
    client.delete()
    schedule.delete()

    assert UserModel.get_by_email("jdfsklj@nxncx") == None
    assert ClientModel.get_by_email("hdjfs@djflkshahahahhaha") == None
    assert ScheduleModel.get_by_status(12345) == None
