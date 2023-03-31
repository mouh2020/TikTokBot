from selenium.webdriver.common.by import By
from .generate_xpath import search_field_xpath,video_author_xpath,video_caption_xpath,video_music_xpath

class MainPageLocators(object) : 
    SEARCH = (By.XPATH,search_field_xpath)
    VIDEO_AUTHOR = (By.XPATH,video_author_xpath)
    VIDEO_CAPTION = (By.XPATH,video_caption_xpath)
    VIDEO_MUSIC = (By.XPATH,video_music_xpath)
class LoginPageLocator(object) : 
    USERNAME = (By.NAME,'username')
    PASSWORD = (By.XPATH,"//input[@placeholder='Password']")
    LOGIN    = (By.TAG_NAME,'button')
class UserPageLocator(object):
    pass
class VideoPageLocator(object) : 
    pass
