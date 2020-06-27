import requests
import json
import jsonpath


url = "https://reqres.in/api/users?page=2"

response = requests.get(url)

json_response = json.loads(response.text)

#print(json_response)

pages = jsonpath.jsonpath(json_response,'total_pages')
#print(pages[0])
assert response.status_code == 200
assert pages[0] == 2

print(response.headers)
print(response.headers.get('Date'))
print(response.headers.get('Server'))

print(response.cookies)
print(response.encoding)
print(response.elapsed)