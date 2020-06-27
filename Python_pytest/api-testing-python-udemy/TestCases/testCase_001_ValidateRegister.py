# python3 -m pytest testCase_001_ValidateRegister.py -v -s

from selenium.webdriver  import Chrome
import pytest

a=101

@pytest.mark.skipif(a>100,reason="Dont want to run for this build")
def test_register_validateData():

    path="/Users/user/Downloads/SW/chromedriver"
    driver = Chrome(executable_path=path)
    driver.get('http://www.thetestingworld.com/testings')
    driver.maximize_window()


def test_register_invalidateData():

    path="/Users/user/Downloads/SW/chromedriver"
    driver = Chrome(executable_path=path)
    driver.get('http://www.thetestingworld.com/testings')
    driver.maximize_window()