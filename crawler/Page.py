from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import bs4

class page:
    def __init__(self, username = ""):
        # step 1
        crawl_time = 0
        parent = None        #in our database

        self.username = username
        self.url = "https://www.instagram.com/"+username+"/"
        self.id = 0
        self.full_name = ""
        self.country_code = ""

        self.is_varified = None
        self.is_private = None
        self.is_business_account = None
        self.is_join_recently = None
        self.business_category_name = None

        self.num_posts = 0
        self.num_follower = 0
        self.num_following = 0
        self.biography = ""
        # step 2
        self.list_following = []
        self.list_follower = []   #in our database
        self.list_pics = []
        # log = []

    def get_meta(self):
        req = requests.get(self.url)
        txt = req.text
        self.id = txt.split('"id":')[1].split(",")[0]
        self.full_name = txt.split('"full_name":')[1].split(",")[0]
        self.biography = txt.split('"biography":')[1].split(",")[0]
        self.num_follower = txt.split('"edge_followed_by":{"count":')[1].split("}")[0]
        self.num_following = txt.split('"edge_follow":{"count":')[1].split("}")[0]
        self.num_posts = txt.split('"edge_owner_to_timeline_media":{"count":')[1].split(",")[0]
        self.country_code = txt.split('"country_code":')[1].split(",")[0]
        self.is_private = txt.split('"is_private":')[1].split(",")[0]
        self.business_category_name = txt.split('"business_category_name":')[1].split(",")[0]
        self.is_join_recently = txt.split('"is_joined_recently":')[1].split(",")[0]
        self.is_business_account = txt.split('"is_business_account":')[1].split(",")[0]
        self.is_varified = txt.split('"is_verified":')[1].split(",")[0]

    def get_following(self, brs):
        brs.get(self.url)
        sleep(5)
        brs.find_element_by_xpath("/html/body/span/section/main/div/header/section/ul/li[3]/a").click()
        sleep(5)
        fl = brs.find_element_by_xpath("/html/body/div[3]/div/div[2]")
        n = 0
        while n < int(self.num_following)-1:
            fl.send_keys(Keys.PAGE_DOWN)
            n = len(brs.find_elements_by_xpath("//a[contains(@class,'FPmhX')]"))
            sleep(0.5)
        for user in brs.find_elements_by_xpath("//a[contains(@class,'FPmhX')]"):
            self.list_following.append(str(user.text))

