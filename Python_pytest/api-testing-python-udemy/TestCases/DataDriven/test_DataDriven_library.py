# python3 -m pytest testCase_001_ValidateRegister.py -v -s
# source env/bin/activate
# pytest -k register Smoke groupTC.py -v -s (Specific test cases)
# pytest -m Smoke groupTC.py -v -s (run group of TC)
# pytest -m "not Smoke" groupTC.py -v -s (not run of TC)
import openpyxl
import requests
import json
from DataDriven import library

def test_Add_New_StudentData():
    url = "http://www.thetestingworldapi.com/api/studentsDetails"
    f = open('/Users/user/Desktop/APIAutomation/api-testing-python-udemy/TestCases/DataDriven/createStudentData.json', 'r')
    json_request = json.loads(f.read())

    obj = library.Common('/Users/user/Desktop/APIAutomation/api-testing-python-udemy/TestCases/DataDriven/studentdata.xlsx','Sheet1')
    col =obj.fetch_col_count()
    row = obj.fetch_excel_rows()
    keylist = obj.fetch_key_name()



    for i in range(2,row+1):
        updated_json_request = obj.update_request_withData(i,json_request,keylist)
        responce = requests.post(url,updated_json_request)
        print(responce.text)