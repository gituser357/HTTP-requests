import requests
import pytest

# создаем функцию post запроса с телом
def test_post_positive_():
    urlpost = "https://petstore.swagger.io/v2/user"
    request = {}
    request['id'] = '987654456987798'
    request['username'] = "qwe"
    request['firstName'] = "kot"
    request['lastName'] = "sobaken"
    request['email'] = "kot@sobaka.ru"
    request['password'] = "qwert"
    request['phone'] = "88005553535"
    request['userStatus'] = "111"

    print("Response: ", request)

    response = requests.post(urlpost, json=request)
    print("Response: ", response.json())

# проверка, что вернулся не пустой id
    assert response.json()['message'] is not None
# проверка, что id в ответе совпал с id в запросе
# message в ответе = id в запросе
    assert response.json()['message'] == request['id']

    urlGet = "https://petstore.swagger.io/v2/user/" + request['username']
    print("urlGet = ", urlGet)
    responseGet = requests.get(urlGet)
    print("response Get = ", responseGet.json())

    number = response.json()['message']

#Добавление ковычек к возвращаемому значению message с последующим сравнением
    NeedNumber = str("'") + number + str("'")
    responseWithQuotes = str("'") + str(responseGet.json()['id']) + str("'")
    assert responseWithQuotes == NeedNumber

def test_post_negative_():
#Отправка пустого запроса
    urlpost = "https://petstore.swagger.io/v2/user"
    request = {}
    print("Response: ", request)
    response = requests.post(urlpost, json=request)
    print("Ответ с пустым body: ", response.json())

#Некорректное id
    request = {}
    request['id'] = '   111'
    request['username'] = "cat"
    request['password'] = "qwert"
    print("Response: ", request)
    response = requests.post(urlpost, json=request)
    print("Ответ с некорректным id : ", response.json())

    urlGet = "https://petstore.swagger.io/v2/user/" + request['username']
    print("urlGet negative = ", urlGet)
    responseGet = requests.get(urlGet)
    print("response Get negative = ", responseGet.json())
