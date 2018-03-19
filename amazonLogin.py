from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def getCode():
	with open('avsLogin.txt', 'r') as inFile:
		loginPage = inFile.read()

	browser = webdriver.Chrome('/Library/Python/2.7/site-packages/selenium/webdriver/chrome/chromedriver')
	browser.get(loginPage)

	email = browser.find_element_by_id("ap_email")
	password = browser.find_element_by_id("ap_password")

	email.send_keys("javierco@umich.edu")
	password.send_keys("Contrera191")

	browser.find_element_by_id("signInSubmit").click()

	redirectUrl = browser.current_url

	pos1 = redirectUrl.find("code=")
	redirectUrl = redirectUrl[pos1+5:]
	pos2 = redirectUrl.find("&")
	code = redirectUrl[0:pos2]

	with open('code.txt', 'w') as outFile:
		outFile.write(code)

if __name__ == '__main__':
	getCode()