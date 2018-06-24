#注释一下
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost/index.php?m=user&c=public&a=reg")
driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys("shaozhen")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("000000")
driver.find_element_by_name("userpassword2").clear()
driver.find_element_by_name("userpassword2").send_keys("000000")
driver.find_element_by_name("mobile_phone").clear()
driver.find_element_by_name("mobile_phone").send_keys("13513513565")
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("12345@qq.com")

driver.find_element_by_class_name("reg_btn").click()
