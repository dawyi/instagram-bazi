from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import bs4

def start():
    firefoxProfile = FirefoxProfile()
    firefoxProfile.set_preference('permissions.default.image', 2)
    browser = webdriver.Firefox(firefoxProfile)
    return browser

def login(brs):
    brs.get("https://www.instagram.com/accounts/login/")
    sleep(5)
    usr = brs.find_element_by_name("username")
    pas = brs.find_element_by_name("password")
    usr.send_keys("USERNAME")
    pas.send_keys("PASSWORD")
    pas.send_keys(Keys.RETURN)
    sleep(5)
    brs.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]").click()

