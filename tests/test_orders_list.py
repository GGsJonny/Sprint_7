import allure
import api


@allure.suite('Тесты получения списка заказов')
class TestGetOrders:
    @allure.title('Успешное получения списка всех заказов')
    @allure.description('Выполняем запрос на получения списка всех заказов')
    def test_get_global_orders(self):
        response = api.get_orders()

        assert response.status_code == 200
        assert "orders" in response.json()