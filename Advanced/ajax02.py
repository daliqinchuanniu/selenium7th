# encoding = utf-8
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By


class TestDemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(10)
        self.driver.quit()

    def test_AjaxDivOptionByIndex(self):
        url = "http://www.sogou.com"
        self.driver.get(url)
        self.driver.find_element(By.ID, "query").send_keys(u"光荣之路")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "ul.suglist :nth-child(3)").click()


if __name__ == '__main__':
    unittest.main()
