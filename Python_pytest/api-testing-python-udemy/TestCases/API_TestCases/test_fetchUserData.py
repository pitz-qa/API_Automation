import requests
import json
import jsonpath
import pytest


url = "https://reqres.in/api/users?page=2"

@pytest.mark.Smoke
def test_get_user_details():
    response = requests.get(url)

    #print(response.content)

    json_responce = json.loads(response.text)
    #print(json_responce)

    pages = jsonpath.jsonpath(json_responce,'total_pages')
    #print(pages[0])

    for i in range(0,6):
        first_name = jsonpath.jsonpath(json_responce,'data['+str(i)+'].first_name')
        print(first_name[0])