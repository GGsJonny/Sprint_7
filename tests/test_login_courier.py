import data
import api
import allure
import helpers


@allure.suite('Тесты логина курьера')
class TestLoginCourier:
    @allure.title('Успешная авторизация курьера')
    @allure.description('Генерируем данные нового курьера, отправляем запрос на его создание и '
                        'авторизацию, проверяем, что логин успешен')
    def test_successful_courier_login(self, created_courier_credentials):
        login_data = helpers.create_login_data(created_courier_credentials)
        login_response = api.login_courier(login_data)

        assert login_response.status_code == 200
        assert "id" in login_response.json()

    @allure.title('Авторизация курьера с неверным логином')
    @allure.description('Генерируем данные нового курьера, отправляем запрос на его создание, '
                        'делаем авторизацию с неверным логином, проверяем наличие ошибки')
    def test_courier_login_with_incorrect_login(self, created_courier_credentials):
        login_data = helpers.create_login_data(created_courier_credentials)
        new_credentials = helpers.generate_new_courier_credentials()
        login_data['login'] = new_credentials['login']

        login_response = api.login_courier(login_data)

        assert login_response.status_code == 404
        assert "message" in login_response.json()
        assert login_response.json()["message"] == data.LOGIN_WITH_INCORRECT_CREDENTIALS_ERROR_TEXT

    @allure.title('Авторизация курьера с неверным паролем')
    @allure.description('Генерируем данные нового курьера, отправляем запрос на его создание, '
                        'делаем авторизацию с неверным паролем, проверяем наличие ошибки')
    def test_courier_login_with_incorrect_password(self, created_courier_credentials):
        login_data = helpers.create_login_data(created_courier_credentials)
        new_credentials = helpers.generate_new_courier_credentials()
        login_data['password'] = new_credentials['password']

        login_response = api.login_courier(login_data)

        assert login_response.status_code == 404
        assert "message" in login_response.json()
        assert login_response.json()["message"] == data.LOGIN_WITH_INCORRECT_CREDENTIALS_ERROR_TEXT

    @allure.title('Авторизация курьера с пустым логином')
    @allure.description('Генерируем данные нового курьера, отправляем запрос на его создание, '
                        'делаем авторизацию с пустым логином, проверяем наличие ошибки')
    def test_courier_login_with_empty_login(self, created_courier_credentials):
        login_data = helpers.create_login_data(created_courier_credentials)
        login_data['login'] = ''

        login_response = api.login_courier(login_data)

        assert login_response.status_code == 400
        assert "message" in login_response.json()
        assert login_response.json()["message"] == data.LOGIN_WITH_EMPTY_FIELD_ERROR_TEXT

    @allure.title('Авторизация курьера с пустым паролем')
    @allure.description('Генерируем данные нового курьера, отправляем запрос на его создание, '
                        'делаем авторизацию с пустым паролем, проверяем наличие ошибки')
    def test_courier_login_with_empty_login(self, created_courier_credentials):
        login_data = helpers.create_login_data(created_courier_credentials)
        login_data['password'] = ''

        login_response = api.login_courier(login_data)

        assert login_response.status_code == 400
        assert "message" in login_response.json()
        assert login_response.json()["message"] == data.LOGIN_WITH_EMPTY_FIELD_ERROR_TEXT