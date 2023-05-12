from .base_page import  BasePage
from utils.locators import *
from loguru import logger
logger.add("selenium_bot.log",format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {function} | {message}",colorize=False,enqueue=True,mode="a")
class LoginPage(BasePage) :
    def __init__(self,driver) :
        self.locator = LoginPageLocator
        super().__init__(driver)
    def enter_username(self,username):  
        self.clear_element_and_send_keys(timeout=30,
                                         element=self.locator.USERNAME,
                                         keys=username,
                                         description='username field')
    def enter_password(self,password) : 
        self.clear_element_and_send_keys(timeout=30,
                                         element=self.locator.PASSWORD,
                                         keys=password,
                                         description='password field')
    def click_login(self) : 
        self.wait_element_to_be_clickabe_and_click(timeout=30,
                                                   element=self.locator.LOGIN,
                                                   description="login button")
        
    def check_login(self,timeout) : 
        if self.locator.SUCCESSFULL_LOGIN in self.get_title() : 
            return True
        elif self.locator.UNSUCCESSFULL_LOGIN in self.get_title() : 
            return False
        else : 
            return False


    

    
    