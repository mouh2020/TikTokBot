from selenium.webdriver.common.by import By
from .generate_xpath import *

class MainPageLocators(object) : 
    SEARCH = (By.XPATH,search_field_xpath())
    #VIDEO = (By.XPATH,video_xpath())

class LoginPageLocator(object) : 
    USERNAME = (By.NAME,'username')
    PASSWORD = (By.XPATH,"//input[@placeholder='Password']")
    LOGIN    = (By.TAG_NAME,'button')
    SUCCESSFULL_LOGIN = 'Watch trending videos for you'
    UNSUCCESSFULL_LOGIN = "Log in | TikTok"
class UserPageLocator(object):
    FOLLOW = (By.XPATH,follow_user_button_xpath())
    USERNAME = (By.XPATH,user_username_xpath())
    NAME = (By.XPATH,user_name_xpath())
    
class VideoPageLocator(object) : 
    LIKE = (By.CSS_SELECTOR,like_video_xpath())
    COMMENT = (By.XPATH,comment_video_xpath())
    
