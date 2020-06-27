import requests
import json
import jsonpath

url = "https://reqres.in/api/users"

def test_create_new_user():
    file = open('/Users/user/Desktop/APIAutomation/GetRequest/postData.json', 'r')
    json_input = file.read()
    requests_json = json.loads(json_input)
    #print(requests_json)
    response = requests.post(url,requests_json)
    print(response.content)
    assert response.status_code == 201
    #print(response.headers.get('Content-Length'))
    response_json1= json.loads(response.text)
    #print(requests_json)
    id = jsonpath.jsonpath(response_json1,'id')
    print(id[0])