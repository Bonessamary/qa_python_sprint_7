import datetime


class URLs:
    main_page_url = 'https://qa-scooter.praktikum-services.ru/'
    #POST Orders - Создание заказа
    creating_order = f'{main_page_url}/api/v1/orders'
    #GET Orders - Получить заказ по его номеру
    order_get_number = f'{main_page_url}/api/v1/orders/track'
    #PUT Orders - Принять заказ
    order_accept = f'{main_page_url}/api/v1/orders/accept'
    #GET Orders - Получение списка заказов courierId
    get_list_orders = f'{main_page_url}/api/v1/orders?courierId='
    #POST Courier - Создание курьера
    create_courier = f'{main_page_url}/api/v1/courier'
    #POST Courier - Логин курьера в системе
    login_courier = f'{main_page_url}/api/v1/courier/login'



class OrderData:

    order_data = {
        "firstName": "Мариночка",
        "lastName": "Буторина",
        "address": "Каноха, дом 16",
        "metroStation": "18",
        "phone": "+7 800 999 16 16",
        "rentTime": 5,
        "deliveryDate": datetime.date.today().day,
        "comment": "Не звонить!",
        "color": []
        }

    color_scooter = [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ]


class Response:
    response_account_not_found = 'Учетная запись не найдена'
    response_no_data_input = "Недостаточно данных для входа"
    response_no_data_account = 'Недостаточно данных для создания учетной записи'
    response_login_used = 'Этот логин уже используется. Попробуйте другой.'
    response_registration_successful = '{"ok":true}'


class LimitPageOrders:
    limit_page_orders = {
        "limit": "5",
        "page": "0"
    }