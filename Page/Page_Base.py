from appium import webdriver

class Base(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, element):
        element_find = self.driver.find_element(element[0],element[1])
        return element_find

    def find_elements(self, element):
        elements_find = self.driver.find_elements(element[0],element[1])
        return elements_find

    def get_windows_size(self):
        return self.driver.get_windows_size()

    # apk包名 com.ehsy.western
    # apk的launcherActivity com.ehsy.western.WelcomeActivity
    def desired_caps(self):
        # apk包名 com.ehsy.western
        # apk的launcherActivity com.ehsy.western.WelcomeActivity
        desired_caps = {
            'platformName': 'Android',
            'deviceName': '127.0.0.1:62001',
            'platformVersion': '7.1.2',
            'appPackage': 'com.ehsy.western',
            'appActivity': 'com.ehsy.western.WelcomeActivity',
            'noReset': True,
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }



