import allure
from methods.order_methods import OrdersMethods


class TestListOrders:

    @allure.title('Проверка получения списка заказов')
    def test_get_list_orders(self):
        list_order = OrdersMethods.list_orders()
        assert list_order.status_code == 200 and "orders" in list_order.json()
