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
    file = open('/Users/user/Desktop/APIAutomation/api-testing-python-udemy/TestCases/StudentmanagmentSys/endToEnd.json','r')
    json_input = file.read()
    requests_json = json.loads(json_input)
    response = requests.post(url, requests_json)
    print(response.content)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])

    tech_url = "http://www.thetestingworldapi.com/api/technicalskills"
    file = open('/Users/user/Desktop/APIAutomation/api-testing-python-udemy/TestCases/StudentmanagmentSys/techDetails.json', 'r')
    json_input = file.read()
    requests_json = json.loads(json_input)
    requests_json['id'] = int(id[0])
    requests_json['st_id'] = id[0]
    response = requests.post(tech_url, requests_json)
    print(response.text)

    add_url = "http://www.thetestingworldapi.com/api/addresses"
    f = open('/Users/user/Desktop/APIAutomation/api-testing-python-udemy/TestCases/StudentmanagmentSys/adress.json','r')
    requests_json = json.loads(f.read())
    requests_json['stId'] = id[0]
    response = requests.post(add_url, requests_json)
    print(response.text)

    finalDetails_url = "http://www.thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response = requests.get(finalDetails_url)
    print(response.text)