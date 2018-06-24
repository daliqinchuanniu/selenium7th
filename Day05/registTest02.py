# encoding = utf-8
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By

import ddt
from Day05.csvFileManager4 import CsvFileManager4


@ddt.ddt
# 为类增加一个装饰器，装饰器类似于javA中的注释
# @ddt.ddt表示这个类实现了数据驱动测试
class RegisterTest02(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()

    data_table = CsvFileManager4().read("data/data04.csv")

    @ddt.data(*data_table)
    # 为test_Register()方法添加装饰器@ddt.data()，制定测试数据data_table,data_table是一个List列表，包含很多元素
    # 在data_table前面加一个星号，表示调用ddt.data()我们传入的不是列表，而是单独的列表中的每一个元素
    # 所以*得作用就是，把列表中每一个元素，都单独看成一个参数。
    def test_Register(self, row):
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.find_element(By.NAME, "username").send_keys(row[0])
        driver.find_element(By.NAME, "password").send_keys(row[1])
        driver.find_element(By.NAME, "userpassword2").send_keys(row[2])
        driver.find_element(By.NAME, "mobile_phone").send_keys(row[3])
        driver.find_element(By.NAME, "email").send_keys(row[4])
        driver.find_element(By.CLASS_NAME, "reg_btn").click()
        time.sleep(3)
        driver.find_element_by_link_text("[退出]").click()
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()