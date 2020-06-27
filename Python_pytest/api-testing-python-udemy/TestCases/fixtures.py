# python3 -m pytest testCase_001_ValidateRegister.py -v -s
# source env/bin/activate
# pytest -k register Smoke groupTC.py -v -s (Specific test cases)
# pytest -m Smoke groupTC.py -v -s (run group of TC)
# pytest -m "not Smoke" groupTC.py -v -s (not run of TC)

from selenium.webdriver  import Chrome
import pytest

@pytest.fixture(scope="module")
def setPath():
    global driver
    path = "/Users/user/Downloads/SW/chromedriver"
    driver = Chrome(executable_path=path)
    yield
    driver.close()

def test_register_validateData(setPath):

    driver.get('http://www.thetestingworld.com/testings')
    driver.maximize_window()

def test_register_invalidateData(setPath):

    driver.get('http://www.thetestingworld.com/testings')
    driver.maximize_window()

def test_invalidate_Data(setPath):

    driver.get('http://www.thetestingworld.com/testings')
    driver.maximize_window()