import pytest
import allure
import requests

from faker import Faker

fake = Faker()
url = 'https://stellarburgers.nomoreparties.site/api'


class TestCreateUser:

    @allure.title('Проверка ручки создания пользователя')
    @allure.description('Сравниваем ожидаемый статус-код ответа "200" с фактическим')
    def test_creating_user_unique_check_status_code(self):
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
        assert r.status_code == 200
        assert r.json()["success"] == True

        r_delete = requests.delete(f"{url}/auth/user", headers=data_auth, data=payload)

    @allure.title('Проверка ручки создания курьера с существующими параметрами (email, password, name)')
    @allure.description('Сравниваем ожидаемый статус-код ответа "403" с фактическим')
    def test_creating_user_duplicate_check_status_code(self):
        email = 'egor@superuser.org'
        password = 'qwerty09876'
        name = 'Egor'
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        r_1 = requests.post(f"{url}/auth/register", data=payload)
        r_2 = requests.post(f"{url}/auth/register", data=payload)
        assert r_2.status_code == 403
        assert r_2.json()["message"] == "User already exists"

    @allure.title('Проверка ручки создания курьера с пустым полем для пароля')
    @allure.description('Сравниваем ожидаемый статус-код ответа "403" с фактическим')
    def test_creating_user_without_password_field_check_status_code(self):
        email = fake.email()
        name = fake.first_name()
        payload = {
            "email": email,
            "name": name
        }
        r_p = requests.post(f"{url}/auth/register", data=payload)
        assert r_p.status_code == 403
        assert r_p.json()["message"] == "Email, password and name are required fields"
