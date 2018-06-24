# encoding = utf-8
import unittest
from selenium.webdriver.common.by import By

import time

from Day05.mytestCase import MyTestCase
from Day05.page_object.loginPage import LoginPage
from Day05.page_object.memberCenterPage import MemberCenterPage


class LoginTest02(MyTestCase):

    def test_Login(self):
        # driver = self.driver
        # driver.get("http://localhost/index.php?m=user&c=public&a=login")
        # driver.find_element(By.ID, "username").send_keys("liyunlong02")
        # driver.find_element(By.ID, "password").send_keys("123456")
        # driver.find_element(By.CSS_SELECTOR, "input.login_btn.fl").click()
        # time.sleep(3)
        # welcome = driver.find_element(By.PARTIAL_LINK_TEXT, "您好").text
        # self.assertIn("您好", welcome, "登录失败")
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.input_username_password("liyunlong02")
        login_page.click_login_button()
        membercenter_page = MemberCenterPage(self.driver)
        self.assertIn("您好", membercenter_page.get_welcom_link_text())


if __name__ == '__main__':
    unittest.main()