from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
class LoginPage(BasePage):
    """By locators"""
    EMAIL=(By.ID,"username")
    PASSWORD=(By.ID,"password")
    LOGIN_BUTTON=(By.ID,"loginBtn")
    SIGNUP_LINK= (By.LINK_TEXT,"Sign up")
    """Constructor"""
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
    """Page actions"""

    """This is used to get title"""
    def get_login_page_title(self,title):
        return  self.get_title(title)
    """ This is use to check sign up link"""
    def is_signup_link_exist(self):
         return self.is_visible(self.SIGNUP_LINK)
    """ this is use to login to app"""
    def do_login(self,username,password):
        self.do_send_key(self.EMAIL,username)
        self.do_send_key(self.PASSWORD,password)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)






