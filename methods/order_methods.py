import requests
import data


class OrdersMethods:
    @staticmethod
    def create_order(body):
        return requests.post(f'{data.Url.BASE_URL}{data.Url.CREATE_ORDER_URL}', json=body)

    @staticmethod
    def list_orders():
        return requests.get(f'{data.Url.BASE_URL}{data.Url.LIST_ORDERS_URL}')


