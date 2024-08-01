import random
import string
import api


def generate_new_courier_credentials(empty_field=None):
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    credentials = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    if empty_field is not None:
        credentials[empty_field] = ""
    return credentials


def create_login_data(credentials):
    return {
        'login': credentials['login'],
        'password': credentials['password']
    }


def login_courier(credentials):
    login_data = create_login_data(credentials)
    login_response = api.login_courier(login_data)
    courier_id = login_response.json().get('id')
    return courier_id


def create_courier(register=False):
    credentials = generate_new_courier_credentials()

    if register:
        api.create_courier(credentials)

    return credentials


def delete_courier(credentials):
    courier_id = login_courier(credentials)
    api.delete_courier(courier_id)