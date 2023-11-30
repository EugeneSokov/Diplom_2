import pytest
import allure
import requests
from faker import Faker

fake = Faker()
url = 'https://stellarburgers.nomoreparties.site/api'


class TestChangeUserData:

    @allure.title('Проверка ручки изменения данных пользователя с авторизацией')
    @allure.description('Сравниваем ожидаемый статус-код ответа "200" с фактическим')
    def test_data_user_data_change_with_auth_check(self, change_user_data):

        assert change_user_data.status_code == 200
        assert change_user_data.json()["success"] == True

    @allure.title('Проверка ручки изменения данных пользователя без авторизации')
    @allure.description('Сравниваем ожидаемый статус-код ответа "401" с фактическим')
    def test_data_user_data_change_without_auth_check(self):
        email_new = fake.email()
        name_new = fake.first_name()
        payload_new = {
            "email": email_new,
            "name": name_new
        }
        r_user_change = requests.patch(f"{url}/auth/user", data=payload_new)

        assert r_user_change.status_code == 401
        assert r_user_change.json()["success"] == False
