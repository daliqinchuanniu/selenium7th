#encoding=utf-8
'''
用unittest框架登录海盗网后台
'''
import unittest
from selenium import webdriver

import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


def highLightElement(river, element):
    river.execute_script("arguments[0].setAttribute('style',arguments[1]);", element, "background:green; border:2px solid red;")

class LoginDemo(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    @classmethod
    def tearDownClass(self):
        time.sleep(10)
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        driver.get("http://localhost/index.php?&m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        
        #\t可以代表TAB键，\n代表Enter
        ActionChains(driver).send_keys("\tpassword").send_keys("\t1234").send_keys("\n").perform()

    def test_product_adding(self):
        driver = self.driver
        driver.find_element_by_link_text("商品管理").click()
        driver.find_element_by_link_text("添加商品").click()
        driver.switch_to.frame(driver.find_element_by_id("mainFrame"))
        textbox = driver.find_element_by_name("name")
        highLightElement(driver, textbox)
        time.sleep(3)
        textbox.send_keys("空调")
        driver.find_element_by_css_selector('a[id="1"]').click()
        driver.find_element_by_css_selector('a[id="2"]').click()
        driver.find_element_by_css_selector('a[id="6"]').click()
        ActionChains(driver).double_click(driver.find_element_by_css_selector('a[id="7"]')).perform()
        Select(driver.find_element_by_name("brand_id")).select_by_visible_text("荣耀(Honor)")
        button = driver.find_element_by_css_selector('input[value="提交"]')
        highLightElement(driver, button)
        time.sleep(3)
        button.click()


if __name__ == '__main__':
    unittest.main()
