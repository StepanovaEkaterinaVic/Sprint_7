import requests
import data


class CourierMethods:
    @staticmethod
    def create_courier(body):
        return requests.post(f'{data.Url.BASE_URL}{data.Url.COURIER_URL}', json=body)

    @staticmethod
    def login_courier(login, password):
        params = {"login": login, "password": password}
        return requests.post(f'{data.Url.BASE_URL}{data.Url.LOGIN_COURIER_URL}/', json=params)

    @staticmethod
    def delete_courier(courier_id):
        return requests.delete(f'{data.Url.BASE_URL}{data.Url.COURIER_URL}/{courier_id}')
