# encoding = utf-8
from selenium.webdriver.common.by import By


class MemberCenterPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "http://localhost/index.php?m=user&c=index&a=index"

    welcome_link_loc = (By.PARTIAL_LINK_TEXT, "您好")

    def get_welcom_link_text(self):
        return self.driver.find_element(*self.welcome_link_loc).text