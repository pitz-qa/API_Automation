# python3 -m pytest test_parameterization.py -v -s

import requests
import json
import jsonpath
import pytest
class TestCases:
    file = open('/Users/user/Desktop/APIAutomation/GetRequest/postData.json', 'r')
    json_input = file.read()
    requests_json = json.loads(json_input)
    @pytest.mark.parametrize("nameJob", requests_json)
    def test_create_new_user(self,nameJob):
        urlPOST = "https://reqres.in/api/users"
        response = requests.post(urlPOST, nameJob)
        print(response.content)
        assert response.status_code == 201
        # print(response.headers.get('Content-Length'))
        response_json1 = json.loads(response.text)
        # print(requests_json)
        id = jsonpath.jsonpath(response_json1, 'id')
        print("New located id is:"+id[0])

    @pytest.mark.parametrize("userIDs", ["2","7"])
    def test_fetch_user_data(self,userIDs):
        urlGET = "https://reqres.in/api/users/"+(userIDs)
        response = requests.get(urlGET)
        json_response = json.loads(response.text)
        #print(json_response)
        data = jsonpath.jsonpath(json_response, 'data')
        print(data)
        assert response.status_code == 200

    @pytest.mark.parametrize("updateUserID", ["2"])
    def test_update_user_data(self,updateUserID):
        urlPut = "https://reqres.in/api/users/"+(updateUserID)
        response = requests.put(urlPut)
        assert response.status_code == 200
        response_json1 = json.loads(response.text)
        updated = jsonpath.jsonpath(response_json1, 'updatedAt')
        print("Updated data is at: "+updated[0])

    @pytest.mark.parametrize("deleteUserID", ["2"])
    def test_delete_user_data(self,deleteUserID):
        urlDELETE = "https://reqres.in/api/users/"+(deleteUserID)
        response = requests.delete(urlDELETE)
        assert response.status_code == 204