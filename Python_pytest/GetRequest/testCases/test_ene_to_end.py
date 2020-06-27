import requests
import json
import jsonpath

App_Url = "http://thetestingworldapi.com/api/studentsDetails"

def add_new_user():
    f = open('/Users/user/Desktop/APIAutomation/GetRequest/newUserData.json','r')
    requests_json = json.loads(f.read())
    response = requests.post(App_Url,requests_json)
    print(response.text)