import pytest
import requests
from faker import Faker

fake = Faker()

url = 'https://stellarburgers.nomoreparties.site/api'


@pytest.fixture()
def login_user():

    email = 'egor@superuser.org'
    password = 'qwerty09876'
    payload = {
        "email": email,
        "password": password,
        }
    r_login = requests.post(f"{url}/auth/login", data=payload)

    return r_login


@pytest.fixture()
def create_user():
    email = fake.email()
    password = fake.password()
    name = fake.first_name()
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    r_register = requests.post(f"{url}/auth/register", data=payload)
    token = r_register.json()["accessToken"]
    data_auth = {
        "authorization": token
    }

    yield r_register

    requests.delete(f"{url}/auth/user", headers=data_auth, data=payload)


@pytest.fixture()
def change_user_data():
    email = fake.email()
    password = fake.password()
    name = fake.first_name()
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    r = requests.post(f"{url}/auth/register", data=payload)
    token = r.json()["accessToken"]
    data_auth = {
        "authorization": token
    }
    email_new = fake.email()
    name_new = fake.first_name()
    payload_new = {
        "email": email_new,
        "name": name_new
    }
    r_user_change = requests.patch(f"{url}/auth/user", headers=data_auth, data=payload_new)

    yield r_user_change

    requests.delete(f"{url}/auth/user", headers=data_auth, data=payload_new)
