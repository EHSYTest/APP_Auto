from appium import webdriver
import time

desired_caps = {
		'platformName': 'Android',
		'deviceName': '127.0.0.1:62001',
		'platformVersion': '7.1.2',
		'appPackage': 'com.ehsy.western',
		'appActivity': 'io.dcloud.PandoraEntry',
		'noReset': True,
		'unicodeKeyboard': True,
		'resetKeyboard': True
	}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.wait_activity("com.ehsy.western.MainActivity", 5)

# print(driver.find_elements_by_id("com.ehsy.western:id/tabIV"))
driver.find_elements_by_id("com.ehsy.western:id/tabIV")[3].click()
time.sleep(2)
driver.find_element_by_xpath('//*[@text="登录/注册"]').click()
driver.find_elements_by_class_name("android.widget.EditText")[0].send_keys('18751551645')
driver.find_elements_by_class_name("android.widget.EditText")[1].send_keys('111qqq')
driver.find_elements_by_xpath('//*[@text="登录"]')[1].click()
