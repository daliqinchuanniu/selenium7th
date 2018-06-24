# encoding = utf-8
"""
1、注册一个用户
2、查询数据库
3、断言注册的数据库是否在数据库中
"""
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import time
from Day05.mytestCase import MyTestCase
from Day06.DBconnection import DBConnection


class RegisterTest(MyTestCase):

    def test_Register(self):
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.find_element(By.NAME, 'username').send_keys("lingdufeng02")
        driver.find_element(By.NAME, "password").send_keys("123456")
        driver.find_element(By.NAME, "userpassword2").send_keys("123456")
        driver.find_element(By.NAME, "mobile_phone").send_keys("14714714778")
        driver.find_element(By.NAME, "email").send_keys("lingdufeng@qq.com")
        driver.find_element(By.CLASS_NAME, "reg_btn").click()
        time.sleep(2)
        new_record = DBConnection().execute_sql_command()
        self.assertEqual("lingdufeng", new_record[0])
        self.assertEqual("lingdufeng@qq.com", new_record[1])
        self.assertEqual("14714714778", new_record[2])
        print(new_record)

if __name__ == '__main__':
    unittest.main()