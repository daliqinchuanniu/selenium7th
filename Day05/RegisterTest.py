# encoding = utf-8
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from Day05.csvFileManager4 import CsvFileManager4


class RegisterTest(unittest.TestCase):
    # 重写setup和teardown()方法
    @classmethod
    # cls一般用于calss，self一般用于普通方法
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(30)
        cls.driver.quit()

    def test_register(self):
        for row in CsvFileManager4().read('data/data.csv'):
            self.driver.get("http://localhost/index.php?m=user&c=public&a=reg")
            self.driver.find_element(By.NAME, 'username').send_keys(row[0])
            self.driver.find_element(By.NAME, "password").send_keys(row[1])
            self.driver.find_element(By.NAME, "userpassword2").send_keys(row[2])
            self.driver.find_element(By.NAME, "mobile_phone").send_keys(row[3])
            self.driver.find_element(By.NAME, "email").send_keys(row[4])
            self.driver.find_element(By.CLASS_NAME, "reg_btn").click()
            time.sleep(5)


if __name__ == '__main__':
    unittest.main()