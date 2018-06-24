# 导入selenium的webdriver代码库
from selenium import webdriver
# 导入时间库
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from telnetlib import EC


driver = webdriver.Chrome()     # 用谷歌浏览器打开一个窗口
#driver = webdriver.Ie()
#driver = webdriver.Firfox()
driver.implicitly_wait(30)      #设置隐式等待时间，一旦找到元素马上执行后面的语句，如果超时仍然找不到元素，那么程序就报错
wait = WebDriverWait(driver, 30)
driver.maximize_window()        # 窗口页面最大化

driver.get("http://localhost/index.php?m=user&c=public&a=login")        # 浏览器打开网址
# 设置页面加载时间，超时之后不再等页面完全加载就执行后续的操作
driver.set_page_load_timeout(10)
driver.find_element_by_id("username").clear()               # 找用户名输入框，并输入内容，
driver.find_element_by_id("username").send_keys("shaozhen") # 这里应该需要先清除一下，以防止之前的占位符影响

driver.find_element_by_id("password").clear()               # 找密码输入窗口，清除，并输入内容
driver.find_element_by_id("password").send_keys("000000")
# 点击登录按钮
driver.find_element_by_class_name("login_btn").click()
# 因为页面加载需要时间，所以需要添加等待时间，要不然后续的定位是基于新加载页面上找的，不等待会找不到而报错。
# 找“进入商城购物”按钮，点击，进入商城页面
driver.find_element_by_link_text("进入商城购物").click()
# 找输入框，清除，并输入需要搜索内容
driver.find_element_by_class_name("input_ss").clear()
driver.find_element_by_class_name("input_ss").send_keys("iphone")
# 找搜索按钮，并点击
driver.find_element_by_class_name("btn1").click()
# 页面跳转，需要等待时间
# 页面中寻找商品图片并点击
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div/div[1]/a/img").click()
# 会新加载一个页面，此时浏览器不止一个页面，而定位符还在原来的页面，需要切换到新的页面
# current = driver.current_window_handle
# allitem = driver.window_handles
#driver.close()
#for item in allitem:
  #     driver.switch_to.window(item)

driver.close()
driver.switch_to.window(driver.window_handles[-1])
# [1]表示元组中第二个元素，[-1]表示元组中最后一个元素。python中元组和列表可以正数从0开始，也可以负着从-1开始，
#driver.switch_to.window(driver.window_handles[1])
#driver.switch_to.window(driver.window_handles[-1])
wait.until(EC.element_to_located_to_be_selected((By.ID, "joinCarButton"))).click()
#river.find_element_by_id("joinCarButton").click()
driver.find_element_by_class_name("shopCar_T_span3").click()
driver.find_element_by_class_name("shopCar_btn_03").click()
