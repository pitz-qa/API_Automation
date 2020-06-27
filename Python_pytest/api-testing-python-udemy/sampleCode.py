from selenium.webdriver  import Chrome

path="/Users/user/Downloads/SW/chromedriver"

driver = Chrome(executable_path=path)

driver.get('http://www.thetestingworld.com/testings')