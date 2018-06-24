# encoding = utf-8
import unittest
from selenium.webdriver.common.by import By

import time

from Day05.mytestCase import MyTestCase


class LoginTest(MyTestCase):

    def test_Login(self):
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        driver.find_element(By.ID, "username").send_keys("liyunlong01")
        driver.find_element(By.ID, "password").send_keys("123456")
        driver.find_element(By.CSS_SELECTOR, "input.login_btn.fl").click()
        time.sleep(3)
        self.assertEqual("我的会员中心 - 道e坊商城 - Powered by Haidao", driver.title)


if __name__ == '__main__':
    unittest.main()