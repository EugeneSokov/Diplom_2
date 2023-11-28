import pytest
import allure
import requests


url = 'https://stellarburgers.nomoreparties.site/api'


class TestCreationOrder:

    @allure.title('Проверка ручки создания заказа неавторизованным пользователем')
    @allure.description('Сравниваем ожидаемый статус-код ответа "200" с фактическим')
    def test_create_order_by_non_authorized_user_check(self):
        r_ingredients = requests.get(f"{url}/ingredients")
        ingr_1 = r_ingredients.json()["data"][1]["_id"]
        ingr_2 = r_ingredients.json()["data"][3]["_id"]
        data_ingredients = {
            "ingredients": [ingr_1, ingr_2]
        }
        r_order = requests.post(f"{url}/orders", data=data_ingredients)

        assert r_order.status_code == 200
        assert r_order.json()["success"] == True

    @allure.title('Проверка ручки создания заказа авторизованным пользователем')
    @allure.description('Сравниваем ожидаемый статус-код ответа "200" с фактическим')
    def test_create_order_by_authorized_user_check(self, login_user):

        r_ingredients = requests.get(f"{url}/ingredients")
        ingr_1 = r_ingredients.json()["data"][1]["_id"]
        ingr_2 = r_ingredients.json()["data"][3]["_id"]
        data_ingredients = {
            "ingredients": [ingr_1, ingr_2]
        }
        token = login_user.json()["accessToken"]
        data_headers = {"accessToken": token}
        r_order = requests.post(f"{url}/orders", headers=data_headers, data=data_ingredients)

        assert r_order.status_code == 200
        assert r_order.json()["success"] == True

    @allure.title('Проверка ручки создания заказа без ингредиентов')
    @allure.description('Сравниваем ожидаемый статус-код ответа "400" с фактическим')
    def test_create_order_by_authorized_user_without_ingredients_check(self, login_user):

        data_ingredients = {
            "ingredients": []
        }
        token = login_user.json()["accessToken"]
        data_headers = {"accessToken": token}
        r_order = requests.post(f"{url}/orders", headers=data_headers, data=data_ingredients)

        assert r_order.status_code == 400
        assert r_order.json()["message"] == 'Ingredient ids must be provided'

    @allure.title('Проверка ручки создания заказа с неверным хешем ингредиентов')
    @allure.description('Сравниваем ожидаемый статус-код ответа "500" с фактическим')
    def test_create_order_by_authorized_user_with_invalid_ids_of_ingredients_check(self, login_user):

        data_ingredients = {
            "ingredients": ["60d3b41abdacab0026a733c6falseids"]
        }
        token = login_user.json()["accessToken"]
        data_headers = {"accessToken": token}
        r_order = requests.post(f"{url}/orders", headers=data_headers, data=data_ingredients)

        assert r_order.status_code == 500
