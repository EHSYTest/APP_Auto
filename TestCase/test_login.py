import unittest,sys
sys.path.append('../Page')
from Page_Base import Base
from Page_Home import Home
from appium import webdriver


class TestLogin(unittest.TestCase):

	def setUp(self):
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
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
		self.driver.wait_activity("com.ehsy.western.MainActivity", 5)
		self.base = Base(self.driver)
		self.home = Home(self.driver)

	def test_login(self):
		self.home.login()

	def tearDown(self):
		print("call teardown")

if __name__ == '__main__':
	unittest.main()