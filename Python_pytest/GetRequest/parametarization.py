import requests
import json
import jsonpath
import pytest

url = "https://reqres.in/api/users"
file = open('/Users/user/Desktop/APIAutomation/GetRequest/postData.json', 'r')
json_input = file.read()
requests_json = json.loads(json_input)
@pytest.mark.parametrize("test_input", requests_json)

def test_create_new_user(test_input):
    response = requests.post(url, test_input)
    print(response.content)
    assert response.status_code == 201
# print(response.headers.get('Content-Length'))
    response_json1 = json.loads(response.text)
# print(requests_json)
    id = jsonpath.jsonpath(response_json1, 'id')
    print(id[0])