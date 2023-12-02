# Ирина Иванова, 11-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data


# Создание нового заказа
def post_new_orders(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,  # подставляем полный url
                         json=body)  # тут тело

response = post_new_orders(data.orders_body);
print(response.status_code)
print(response.json())

# Сохранение номера трека заказа
track_order = response.json()["track"]

# Получение заказа по треку заказа
def get_orders(track_order):
    return requests.get(configuration.URL_SERVICE + configuration.REQUEST_ORDER_TRACK,
                        params={"t": track_order})


print(response.status_code)
print(response.json())
