import allure
from methods.courier_methods import CourierMethods


class TestCreateCourier:
    @allure.title('Проверка успешного создания аккаунта курьера')
    @allure.description('Проверка кода ответа и тела ответа')
    def test_success_create_courier(self, generate_new_courier_data):
        response = CourierMethods.create_courier(generate_new_courier_data[0])
        assert response.status_code == 201
        assert response.json() == {'ok': True}

    @allure.title('Проверка получения ошибки при повторном использовании логина для создания курьера')
    @allure.description('Проверка кода ответа и тела ответа')
    def test_create_courier_with_conflict_login(self, generate_new_courier_data):
        CourierMethods.create_courier(generate_new_courier_data[0])
        response_conflict = CourierMethods.create_courier(generate_new_courier_data[0])
        assert response_conflict.status_code == 409
        r = response_conflict.json()
        assert r.get('message') == "Этот логин уже используется. Попробуйте другой."

    @allure.title('Проверка получения ошибки при отсутствии логина для создания курьера')
    @allure.description('Проверка кода ответа и тела ответа')
    def test_create_courier_without_login(self, generate_new_courier_data):
        response = CourierMethods.create_courier(generate_new_courier_data[2:4])
        assert response.status_code == 400
        r = response.json()
        assert r.get('message') == "Недостаточно данных для создания учетной записи"

    @allure.title('Проверка получения ошибки при отсутствии пароля для создания курьера')
    @allure.description('Проверка кода ответа и тела ответа')
    def test_create_courier_without_password(self, generate_new_courier_data):
        response = CourierMethods.create_courier([generate_new_courier_data[1], generate_new_courier_data[3]])
        assert response.status_code == 400
        r = response.json()
        assert r.get('message') == "Недостаточно данных для создания учетной записи"
