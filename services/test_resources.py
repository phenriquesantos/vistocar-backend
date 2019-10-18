import pytest
import requests

from datetime import date

from models.user import UserModel
from models.client import ClientModel
from models.phone import PhoneModel
from models.schedule import ScheduleModel


def setup_():
    # create client
    user = UserModel()
    user.first_name = 'teste'
    user.last_name = 'teste'
    user.email = 'jdfsklj@nxncx'
    user.password = 'sjdfjljslfdsj'
    user.timestamp = date.today()
    user.save()

    # create client
    client = ClientModel()
    client.first_name = 'teste'
    client.last_name = 'teste'
    client.cpf = 69328462
    client.rg_number = 654987362
    client.rg_uf = 'sp'
    client.email = 'hdjfs@djflks'
    client.password = 'kjdslksjl'
    client.timestamp = date.today()
    client.save()

    # create schedule
    scheduling = ScheduleModel()
    scheduling.status = 64365983294
    scheduling.created_at = 76
    scheduling.client_id = 57
    scheduling.last_update = 87
    scheduling.timestamp = date.today()
    scheduling.save()

# test user
def test_post_user():
    assert 1 == 1

def test_get_user():
    response = requests.get('https://localhost:5000/api/user')
    assert response.status_code == 200

def test_put_user():
    assert 1 == 1

# test client
def test_post_client():
    assert 1 == 1

def test_get_client():
    response = requests.get('https://localhost:5000/api/client')
    assert response.status_code == 200

def test_put_client():
    assert 1 == 1

# test schedule
def test_post_schedule():
    assert 1 == 1

def test_get_schedule():
    response = requests.get('https://localhost:5000/api/schedule')
    assert response.status_code == 200

def test_put_schedule():
    assert 1 == 1

# test destroy
def test_destroy():
    user = UserModel.get_by_email('jdfsklj@nxncx')
    client = ClientModel.get_by_email('hdjfs@djflks')
    schedule = ScheduleModel.get_by_status(64365983294)

    user.delete()
    client.delete()
    schedule.delete()

    assert UserModel.get_by_email('jdfsklj@nxncx') == None
    assert ClientModel.get_by_email('hdjfs@djflks') == None
    assert ScheduleModel.get_by_status(64365983294) == None
