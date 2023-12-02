# Ирина Иванова, 11-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request

# Функция для позитивной проверки
def positive_assert(track_order):
    # В переменную order_respons сохраняется результат запроса на получение заказа по треку заказа
    order_response = sender_stand_request.get_orders(track_order)
    # Проверяется, что код ответа равен 200
    assert order_response.status_code == 200


# Тест 1. Проверка, что получен успешный ответ
def test_get_order_track_success_response():
    positive_assert(sender_stand_request.track_order)
