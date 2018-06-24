# encoding = utf-8
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestDemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    def test_AjaxDivOptionByKeys(self):
        url = "http://www.sogou.com"
        self.driver.get(url)

        searchBox = self.driver.find_element(By.ID, "query")
        searchBox.send_keys(u"光荣之路")
        time.sleep(2)
        for loop in range(3):
            searchBox.send_keys(Keys.DOWN)
            time.sleep(0.5)

        searchBox.send_keys(Keys.ENTER)
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()