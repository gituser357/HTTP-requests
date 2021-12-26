def test_post_positive_():
    url = "https://petstore.swagger.io/v2/pet"
    request = {}
    request['name'] = "kek"
    request['category'] = {}
    request['category'] ['name'] = "lol"
    request['photoUrls'] = ['lolik']
    print("request", request)