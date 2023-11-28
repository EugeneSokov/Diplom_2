import pytest
import allure
import requests


url = 'https://stellarburgers.nomoreparties.site/api'


class TestObtainAllOrders:

    @allure.title('Проверка ручки получения заказов авторизованным пользователем')
    @allure.description('Сравниваем ожидаемый статус-код ответа "200" с фактическим')
    def test_obtaining_all_orders_by_authorized_user_check(self, login_user):

        r_ingredients = requests.get(f"{url}/ingredients")
        ingr_1 = r_ingredients.json()["data"][0]["_id"]
        ingr_2 = r_ingredients.json()["data"][2]["_id"]
        ingr_3 = r_ingredients.json()["data"][3]["_id"]
        data_ingredients = {
            "ingredients": [ingr_1, ingr_2, ingr_3]
        }
        token = login_user.json()["accessToken"]
        data_auth = {
            "authorization": token
        }
        r_all_orders = requests.get(f"{url}/orders", headers=data_auth)
        assert r_all_orders.status_code == 200
        assert r_all_orders.json()["success"] == True

    @allure.title('Проверка ручки получения заказов неавторизованным пользователем')
    @allure.description('Сравниваем ожидаемый статус-код ответа "401" с фактическим')
    def test_obtaining_all_orders_by_non_authorized_user_check(self):

        r_all_orders = requests.get(f"{url}/orders")

        assert r_all_orders.status_code == 401
        assert r_all_orders.json()["success"] == False
