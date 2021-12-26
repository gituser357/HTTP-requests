import requests
import pytest

def test_post_positive_():
    url = "https://petstore.swagger.io/v2/pet"
    request = {}
    request['name'] = "kek"
    request['category'] = {}
    request['category'] ['name'] = "lol"
    request['photoUrls'] = ['lolik']
    print("request", request)

    response = requests.post(url, json=request)
    print("ответ", response.json())
# проверка что вернулся не пустой id
    assert response.json()['id'] is not None
# проверка что имя в ответе совпало с именем в запросе
    assert response.json()['name'] == request['name']

    urlGet = "https://petstore.swagger.io/v2/pet/" + str(response.json()['id'])

    responseGet = requests.get(urlGet)
    print('urlGet = ', urlGet)
    responseGet = requests.get(urlGet)
    print('response GEt = ', responseGet.json())

    assert responseGet.json()['id'] == response.json()['id']
    assert responseGet.json()['name'] == response.json()['name']

def test_post_negative_():
    url = "https://petstore.swagger.io/v2/pet"
    request = {}
    request['name'] = [] #
    request['category'] = {}
    request['category'] ['name'] = "lol"
    request['photoUrls'] = ['lolik']
    print("request", request)

    response = requests.post(url, json=request)
    print("ответ", response.json())

    assert response.json()['message'] == 'something bad happened'

