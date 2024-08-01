import pytest
import allure
import data
import api
import helpers


@allure.suite('Тесты на создание курьера')
class TestCreateCourier:
    @allure.title('Создание курьера')
    @allure.description('Генерируем данные нового курьера, отправляем запрос на его создание и проверяем ответ')
    def test_create_courier(self, courier_credentials):
        create_response = api.create_courier(courier_credentials)

        assert create_response.status_code == 201
        assert "ok" in create_response.json() and create_response.json()["ok"] is True

    @allure.title('Создание двух одинаковых курьеров')
    @allure.description('Генерируем данные нового курьера, отправляем два запроса на его создание, '
                        'проверяем, что второй запрос возвращает нужную ошибку')
    def test_create_duplicated_courier(self, courier_credentials):
        create_response = api.create_courier(courier_credentials)
        assert create_response.status_code == 201

        create_response2 = api.create_courier(courier_credentials)
        assert create_response2.status_code == 409
        assert "message" in create_response2.json()
        assert create_response2.json()["message"] == data.CREATE_COURIER_DUPLICATION_ERROR_TEXT

    @allure.title('Создание курьера с пустым обязательным полем')
    @allure.description('Генерируем данные нового курьера с пустым обязательным полем (логин или пароль), '
                        'отправляем запрос на его создание, проверяем, что запрос возвращает нужную ошибку')
    @pytest.mark.parametrize(
        'credentials',
        [
            helpers.generate_new_courier_credentials(empty_field='login'),
            helpers.generate_new_courier_credentials(empty_field='password')
        ]
    )
    def test_create_courier_with_empty_login_or_password(self, credentials):
        create_response = api.create_courier(credentials)

        assert create_response.status_code == 400
        assert "message" in create_response.json()
        assert create_response.json()["message"] == data.CREATE_COURIER_EMPTY_FIELD_ERROR_TEXT

    @allure.title('Создание курьера с пустым именем')
    @allure.description('Генерируем данные нового курьера с пустым именем, '
                        'отправляем запрос на его создание и проверяем ответ')
    def test_create_courier_with_empty_name(self, courier_credentials):
        courier_credentials['firstName'] = ''
        create_response = api.create_courier(courier_credentials)
        response_json = create_response.json()

        assert create_response.status_code == 201
        assert "ok" in response_json and response_json["ok"] is True