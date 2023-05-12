from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.video_page import VideoPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium_stealth import stealth

options = Options()
options.add_argument("--user-data-dir=/home/med/.config/google-chrome/")
driver=webdriver.Chrome(options=options)
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Linux",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
base_page = BasePage(driver)
video_page = VideoPage(driver=driver)
video_page.open_video_url("arc_journal",7197913785313594667)
video_page.like_video(like_with_keyboad=False)
time.sleep(10)



