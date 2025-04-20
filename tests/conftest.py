import pytest
from generators import generate_courier_body
from methods.courier_methods import CourierMethods


@pytest.fixture(scope="class")
def generate_new_courier_data():
    courier_body = generate_courier_body()
    login = courier_body['login']
    password = courier_body['password']
    firstname = courier_body['firstname']
    yield [courier_body, login, password, firstname]
    response = CourierMethods.login_courier(login, password)
    if response.status_code == 200:
        CourierMethods.delete_courier(response.json()['id'])
