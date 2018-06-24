
#2、进入商品管理模块
#3、点击添加商品链接
#4、输入商品名称
#5、选择商品分类
#6、在下拉框中选择商品品牌
#7、提交
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost/index.php?&m=admin&c=public&a=login")
driver.implicitly_wait(30)
#1、登录海盗网后台
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_class_name("Btn").click()

driver.find_element_by_link_text("商品管理").click()
driver.find_element_by_link_text("添加商品").click()
driver.switch_to.frame('mainFrame')
driver.find_element_by_name("name").send_keys("饮水机")
