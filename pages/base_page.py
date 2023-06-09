from loguru import logger
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
logger.add("selenium_bot.log",format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {function} | {message}",colorize=False,enqueue=True,mode="w")
class BasePage(object) :
    def __init__(self,driver) : 
        self.driver   = driver
        self.base_url = "https://www.tiktok.com/"
    def get_title(self) :
        try : 
            logger.info(f'{self.driver.title}')
            return self.driver.title
        except Exception as e :
            logger.error(f'error : {e}') 
    def open_login_page(self, url):
        try : 
            url = self.base_url+"login/phone-or-email/email"
            logger.info(f' {url}')
            self.driver.get(url)
        except Exception as e :
            logger.error(f'error : {e}') 
    def open_video_url(self,username,video_id) : 
        try : 
            url = self.base_url+"@"+username+"/video/"+str(video_id)
            logger.info(f' {url}')
            self.driver.get(url)
        except Exception as e : 
            logger.error(f'error : {e}') 
    def open_user_url(self,username) : 
        try : 
            url = self.base_url+"@"+username
            logger.info(f' {url}')
            self.driver.get(url)
        except Exception as e : 
            logger.error(f'error : {e}') 
    def wait_element_to_be_clickable(self,timeout,element,description=None) : 
        try :
            logger.info(f'{description}')
            WebDriverWait(self.driver,timeout).until(EC.element_to_be_clickable(element))
        except Exception as e : 
            logger.error(f"error : {e}")
    def wait_element_to_be_clickabe_and_click(self,timeout,element,description=None) : 
        try :
            logger.info(f'{description}')
            WebDriverWait(self.driver,timeout).until(EC.element_to_be_clickable(element)).click()
        except Exception as e : 
            logger.error(f"error : {e}")
    def wait_element_to_be_clickabe_and_send_keys(self,keys,timeout,element,description=None) : 
        try :
            logger.info(f'{description}')
            WebDriverWait(self.driver,timeout).until(EC.element_to_be_clickable(element)).send_keys(keys)
        except Exception as e : 
            logger.error(f"error : {e}")
    def clear_element_and_send_keys(self,keys,timeout : int,element:tuple ,description=None): 
        try : 
            logger.info(f'{description}')
            WebDriverWait(self.driver,timeout).until(EC.element_to_be_clickable(element)).clear()
            WebDriverWait(self.driver,timeout).until(EC.element_to_be_clickable(element)).send_keys(keys)
        except Exception as e : 
            logger.error(f'error {e}')
    


