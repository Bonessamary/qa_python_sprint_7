import allure
import helpers


class TestListOrder:
    @allure.title("Тестирование получения списка заказов")
    def test_order_list(self):
        body = helpers.GetOrder.set_param_order_list(self)
        responce_data = helpers.GetOrder.get_orders_list(body)
        assert 200 == responce_data.status_code and type(responce_data.json()["orders"]) == list