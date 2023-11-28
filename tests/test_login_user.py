import pytest
import allure
import requests


url = 'https://stellarburgers.nomoreparties.site/api'


class TestLoginUser:

    @allure.title('Проверка ручки логина пользователя с валидным набором (email, password)')
    @allure.description('Сравниваем ожидаемый статус-код ответа "200" с фактическим')
    def test_login_user_check(self, login_user):

        assert login_user.status_code == 200
        assert login_user.json()["success"] == True

    @allure.title('Проверка ручки логина пользователя с неверным логином')
    @allure.description('Сравниваем ожидаемый статус-код ответа "401" с фактическим')
    def test_login_user_false_login_check(self):
        email = '__egor@superuser.org'
        password = 'qwerty09876'
        name = 'Egor'
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        r = requests.post(f"{url}/auth/login", data=payload)
        assert r.status_code == 401
        assert r.json()["message"] == "email or password are incorrect"

    @allure.title('Проверка ручки логина пользователя с неверным паролем')
    @allure.description('Сравниваем ожидаемый статус-код ответа "401" с фактическим')
    def test_login_user_false_password_check(self):
        email = 'egor@superuser.org'
        password = '_qwerty09876_'
        name = 'Egor'
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        r = requests.post(f"{url}/auth/login", data=payload)
        assert r.status_code == 401
        assert r.json()["message"] == "email or password are incorrect"
