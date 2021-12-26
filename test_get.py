import requests
import pytest

def test_get_positive():
# Запрос на проверку пользователя по имени
    url = "https://petstore.swagger.io/v2/user/qwe"
    response = requests.get(url)
    print("response Get = ", response)

def test_get_negative():
# Выход из сессии без идентификаторов изначально как в swagger
    url = "https://petstore.swagger.io/v2/user/logout"
    response = requests.get(url)
    print("response Get log out = ", response.json())