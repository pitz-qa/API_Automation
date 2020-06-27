# python3 -m pytest testCase_001_ValidateRegister.py -v -s
# source env/bin/activate
# pytest -k register Smoke groupTC.py -v -s (Specific test cases)
# pytest -m Smoke groupTC.py -v -s (run group of TC)
# pytest -m "not Smoke" groupTC.py -v -s (not run of TC)

import requests
import json
import jsonpath
import pytest


def test_Add_New_StudentData():
    url = "http://www.thetestingworldapi.com/api/studentsDetails"
    file = open('/Users/user/Desktop/APIAutomation/api-testing-python-udemy/TestCases/StudentmanagmentSys/createStudentData.json','r')
    json_input = file.read()
    requests_json = json.loads(json_input)
    response = requests.post(url, requests_json)
    print(response.content)

def test_Update_StudentData():
    url = "http://www.thetestingworldapi.com/api/studentsDetails/178324,"
    file = open('/Users/user/Desktop/APIAutomation/api-testing-python-udemy/TestCases/StudentmanagmentSys/updateStudentdata.json','r')
    json_input = file.read()
    requests_json = json.loads(json_input)
    response = requests.put(url, requests_json)
    print(response.content)

def test_get_StudentDetails():
    url = "http://www.thetestingworldapi.com/api/studentsDetails/178324"
    response = requests.get(url)
    # json_responce = json.loads(response.text) OR
    json_responce = response.json()
    print(json_responce)
    id = jsonpath.jsonpath(json_responce,'data.id')
    assert id[0] ==178324

#def test_delete_Student():
#    url = "http://www.thetestingworldapi.com/api/studentsDetails/178307"
#    response = requests.delete(url)
#    print(response.text)