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

def test_basicAuth():
    responce = requests.get("https://github.com/user", auth=HTTPBasicAuth('piyushtheunique@gmail.com','Piyush@007'))
    print(responce.content)