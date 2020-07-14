import sys
sys.path.append('../Page')
from Page_Base import Base
from appium.webdriver.common.mobileby import By
import time

class Home(Base):

    my_ehsy = (By.ID, "com.ehsy.western:id/tabIV")
    login_ehsy = (By.XPATH,'//*[@text="登录/注册"]')
    login_name = (By.CLASS_NAME, "android.widget.EditText")
    login_password = (By.CLASS_NAME, "android.widget.EditText")
    login_button = (By.XPATH, '//*[@text="登录"]')

    def login(self):
        self.find_elements(self.my_ehsy)[3].click()
        time.sleep(2)
        self.find_element(self.login_ehsy).click()
        time.sleep(2)
        self.find_elements(self.login_name)[0].send_keys('18751551645')
        self.find_elements(self.login_password)[1].send_keys('111qqq')
        self.find_elements(self.login_button)[1].click()
