# encoding = utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Day05.mytestCase import MyTestCase
import unittest


driver = webdriver.Chrome()
driver.get("http://localhost/index.php?m=user&c=public&a=login")
driver.find_element(By.ID, "username").send_keys("liyunlong01")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "input.login_btn.fl").click()
WebDriverWait(driver, 20, 0.5).until(EC.visibility_of_element_located((By.LINK_TEXT, "进入商城购物")))

driver.find_element_by_link_text("进入商城购物").click()