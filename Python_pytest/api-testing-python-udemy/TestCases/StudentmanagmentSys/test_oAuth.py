# python3 -m pytest testCase_001_ValidateRegister.py -v -s
# source env/bin/activate
# pytest -k register Smoke groupTC.py -v -s (Specific test cases)
# pytest -m Smoke groupTC.py -v -s (run group of TC)
# pytest -m "not Smoke" groupTC.py -v -s (not run of TC)

import requests
from requests.auth import HTTPBasicAuth
import json
import jsonpath
import pytest

def test_oAuth():
    tocken_URL = "URL"
    data = {'grant_type':"value",'username':'value','password':'value'}
    responce =requests.post(tocken_URL,data)
    tocken_value = jsonpath.jsonpath(responce.json(),'access_token')

    auth = {'Authorization':'Barer '+tocken_value[0]}
    APP_URL = "http://www.thetestingworldapi.com/api/StDetails/1104"
    responce = requests.get(APP_URL)
    print(responce.text)