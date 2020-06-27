# python3 -m pytest testCase_001_ValidateRegister.py -v -s
# source env/bin/activate
# pytest -k register Smoke groupTC.py -v -s (Specific test cases)
# pytest -m Smoke groupTC.py -v -s (run group of TC)
# pytest -m "not Smoke" groupTC.py -v -s (not run of TC)

import requests
import json
import jsonpath
import pytest


def test_add_New_Student():
    global id
    url = "http://www.thetestingworldapi.com/api/studentsDetails"
    file = open('/Users/user/Desktop/APIAutomation/api-testing-python-udemy/TestCases/StudentmanagmentSys/request_chaining.json','r')
    requests_json = json.loads(file.read())
    response = requests.post(url, requests_json)
    # print(response.content)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])

def test_get_student_data():
    url = "http://www.thetestingworldapi.com/api/studentsDetails/"+str(id[0])
    responce = requests.get(url)
    print(responce.text)