import requests
import json
import jsonpath

url = "https://reqres.in/api/users/2"

file = open('/Users/user/Desktop/APIAutomation/api-testing-python-udemy/postRequest/createUserData.json','r')
json_input = file.read()
requests_json = json.loads(json_input)
#print(requests_json)

response = requests.put(url,requests_json)
print(response.content)

assert response.status_code == 200

# print(response.headers.get('Content-Length'))

response_json1= json.loads(response.text)
# print(requests_json)

updated = jsonpath.jsonpath(response_json1,'updatedAt')
print(updated[0])