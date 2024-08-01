import pytest
import data
import allure
import api


@allure.suite('Тесты создания заказа')
class TestCreateOrders:
    @allure.title('Успешное создание заказа')
    @allure.description('Генерируем данные о заказе, отправляем запрос на его создание и проверяем ответ')
    @pytest.mark.parametrize(
        'order_info',
        [
            data.ORDER_INFO_WITHOUT_COLOR,
            data.ORDER_INFO_COLOR_BLACK,
            data.ORDER_INFO_COLOR_GREY,
            data.ORDER_INFO_COLOR_BLACK_AND_GREY
        ]
    )
    def test_successful_order_creation(self, order_info):
        response = api.create_order(order_info)

        assert response.status_code == 201
        assert "track" in response.json()