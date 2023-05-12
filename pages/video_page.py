from .base_page import  BasePage
from utils.locators import VideoPageLocator
from loguru import logger
logger.add("selenium_bot.log",format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {function} | {message}",colorize=False,enqueue=True,mode="a")
class VideoPage(BasePage) :
    def __init__(self,driver) :
        self.locator = VideoPageLocator
        super().__init__(driver)
        
    def like_video(self,like_with_keyboad=None) :
        if like_with_keyboad : 
            # l is a shortcut to like a video
            self.wait_element_to_be_clickabe_and_send_keys(element=self.locator.LIKE,
                                                          timeout=30,
                                                          keys="l",
                                                          description="like_button"
                                                          )

        else : 
            self.wait_element_to_be_clickabe_and_click(element=self.locator.LIKE,
                                                       timeout=30,
                                                       description="like button",
                                                       )