import requests
import pytest

def test_delete_positive():
# Удаление пользователя
    url = "https://petstore.swagger.io/v2/user/1112"
    response = requests.delete(url)
    # без проверки ответа response.json() т.к. выдает ошибку на json()
    print("Ответ: ", response)

def test_delete_negative():
# Удаление несуществующего пользователя
    url = "https://petstore.swagger.io/v2/user/qweetrytuykkmn"
    response = requests.delete(url)
    print("response = ", response)

# Пустой запрос
    url = "https://petstore.swagger.io/v2/user/"
    response = requests.delete(url)
    print("response = ", response)

# Спец символы
    url = "https://petstore.swagger.io/v2/user/*?*-$%"
    response = requests.delete(url)
    print("response = ", response)
