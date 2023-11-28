import pytest
import requests


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


