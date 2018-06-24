# encoding = utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "http://localhost/index.php?m=user&c=public&a=login"

    username_input_loc = (By.ID, "username")
    # 声明一个元组，元素分别是By.ID, "username"
    password_input_loc = (By.ID, "password")
    # 声明一个元组，元素分别是By.ID, "password"
    click_button_loc = (By.CSS_SELECTOR, "input.login_btn.fl")

    def open(self):
        self.driver.get(self.url)

    def input_username_password(self, username='liyunlong01', password='123456'):
        self.driver.find_element(*self.username_input_loc).send_keys(username)
        # *self.username_input_loc中 * 代表传入的是元组中单独的元素，而不是一个元组
        self.driver.find_element(*self.password_input_loc).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.click_button_loc).click()