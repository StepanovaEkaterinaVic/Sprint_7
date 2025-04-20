import allure
import random

from generators import generate_courier_body
from methods.courier_methods import CourierMethods


class TestLoginCourier:
    @allure.title('Проверка успешного входа в аккаунт курьера')
    @allure.description('Проверка кода ответа и тела ответа')
    def test_success_login_courier(self, generate_new_courier_data):
        CourierMethods.create_courier(generate_new_courier_data[0])
        response = CourierMethods.login_courier(generate_new_courier_data[1], generate_new_courier_data[2])
        assert response.status_code == 200 and "id" in response.json()

    @allure.title('Проверка получения ошибки при вводе неправильного пароля при входе в аккаунт курьера')
    @allure.description('Проверка кода ответа и тела ответа')
    def test_login_courier_wrong_password(self, generate_new_courier_data):
        CourierMethods.create_courier(generate_new_courier_data[0])
        response = CourierMethods.login_courier(generate_new_courier_data[1], random.randint(1000, 9999))
        assert (response.status_code == 404 and response.json().get("message") == "Учетная запись не найдена")

    @allure.title('Проверка получения ошибки при вводе неправильного логина при входе в аккаунт курьера')
    @allure.description('Проверка кода ответа и тела ответа')
    def test_login_courier_wrong_password(self, generate_new_courier_data):
        CourierMethods.create_courier(generate_new_courier_data[0])
        wrong_login = generate_courier_body()
        login_value = wrong_login["login"]
        response = CourierMethods.login_courier(login_value, generate_new_courier_data[2])
        assert (response.status_code == 404 and response.json().get("message") == "Учетная запись не найдена")

    @allure.title('Проверка получения ошибки при отсутствии логина при входе в аккаунт курьера')
    @allure.description('Проверка кода ответа и тела ответа')
    def test_login_courier_without_login(self, generate_new_courier_data):
        CourierMethods.create_courier(generate_new_courier_data[0])
        response = CourierMethods.login_courier("", generate_new_courier_data[2])
        assert (response.status_code == 400 and response.json().get("message") == "Недостаточно данных для входа")

    @allure.title('Проверка получения ошибки при отсутствии пароля при входе в аккаунт курьера')
    @allure.description('Проверка кода ответа и тела ответа')
    def test_login_courier_without_password(self, generate_new_courier_data):
        CourierMethods.create_courier(generate_new_courier_data[0])
        response = CourierMethods.login_courier(generate_new_courier_data[1], 0)
        assert (response.status_code == 400 and response.json().get("message") == "Недостаточно данных для входа")

    @allure.title('Проверка получения ошибки при отсутствии заполнения полей логин, пароль при входе в аккаунт курьера')
    @allure.description('Проверка кода ответа и тела ответа')
    def test_login_courier_without_login_and_password(self, generate_new_courier_data):
        CourierMethods.create_courier(generate_new_courier_data[0])
        response = CourierMethods.login_courier("", 0)
        assert (response.status_code == 400 and response.json().get("message") == "Недостаточно данных для входа")

    @allure.title('Проверка получения ошибки при входе в аккаунт курьера для несуществующего пользователя')
    @allure.description('Проверка кода ответа и тела ответа')
    def test_login_courier_without_login_and_password(self):
        wrong_courier = generate_courier_body()
        login_value = wrong_courier["login"]
        password_value = wrong_courier["password"]
        response = CourierMethods.login_courier(login_value, password_value)
        assert (response.status_code == 404 and response.json().get("message") == "Учетная запись не найдена")

