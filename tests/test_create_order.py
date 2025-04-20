import allure
import pytest

from generators import generate_order_body
from methods.order_methods import OrdersMethods


class TestCreateOrder:

    @allure.title('Тест на успешное создание заказа')
    @allure.description('Проверка кода ответа и тела ответа')
    @pytest.mark.parametrize("color_scooter", [
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"],
            [None]
        ])
    def test_create_order(self, color_scooter):
        order = OrdersMethods.create_order(generate_order_body(color_scooter))
        assert order.status_code == 201 and "track" in order.json()
