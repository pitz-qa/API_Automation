# python3 -m pytest testCase_001_ValidateRegister.py -v -s
# source env/bin/activate
# pytest -k register Smoke groupTC.py -v -s (Specific test cases)
# pytest -m Smoke groupTC.py -v -s (run group of TC)
# pytest -m "not Smoke" groupTC.py -v -s (not run of TC)

import requests
import json
import jsonpath
import pytest

url = "https://reqres.in/api/users"

@pytest.fixture()
def start_exe():
    global file,response
    file = open('/Users/user/Desktop/APIAutomation/api-testing-python-udemy/TestCases/API_TestCases/createUserData.json', 'r')
    json_input = file.read()
    requests_json = json.loads(json_input)
    # print(requests_json)
    response = requests.post(url, requests_json)
    print(response.content)

@pytest.mark.Smoke
def test_create_new_user(start_exe):
    assert response.status_code == 201
    # print(response.headers.get('Content-Length'))
    response_json1= json.loads(response.text)
    # print(requests_json)
    id = jsonpath.jsonpath(response_json1,'id')
    print(id[0])

@pytest.mark.Sanity
def test_create_other_user(start_exe):
    assert response.status_code == 201
    response_json1= json.loads(response.text)
    id = jsonpath.jsonpath(response_json1,'id')
    print(id[0])