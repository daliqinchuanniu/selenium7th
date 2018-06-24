#selenium执行JS中的两个关键字，return和arguments
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost/")
driver.implicitly_wait(30)

'''
某些元素，用selenium比JS的方法寻找的容易，但是selenium没法removeAttribute等方法，
所以需要将selenium元素转换成JS的元素，这样就不用childNodes这些方法了，
就是把两种方法结合起来
'''
login_link = driver.find_element_by_link_text("登录")
driver.execute_script("arguments[0].removeAttribute('target')", login_link)
#arguments是参数数组，指的是js后面的第一个字符串，一般情况只用到arguments[0]
login_link.click()

driver.find_element_by_id("username").send_keys("shaozhen")
ActionChains(driver).send_keys(Keys.TAB).send_keys("000000").perform()
#driver.find_element_by_id("password").send_keys("000000")
driver.find_element_by_css_selector("input[value='登　录']").click()

driver.find_element_by_link_text("进入商城购物").click()

driver.find_element_by_name("keyword").clear()
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_class_name("btn1").click()
#将商品的target属性去掉，再点击图片
#css定位比较长，适当截短
iphone = driver.find_element_by_css_selector("div.protect_con > div > div.shop_01-imgbox > a")
driver.execute_script("arguments[0].removeAttribute('target')", iphone)
iphone.click()
#加入购物车
driver.find_element_by_css_selector(".goods-pay-btn-c.goods-add").click()
#去购物车结算
driver.find_element_by_class_name("shopCar_T_span3").click()
#结算
driver.find_element_by_link_text("结算").click()
#添加地址
driver.find_element_by_css_selector(".add-address").click()
#
driver.find_element_by_class_name("add-new-name-span").send_keys("零度风")
ActionChains(driver).send_keys(Keys.TAB).send_keys("13513513565").perform()

#下拉框是一种特殊的网页元素，对下拉框的操作了普通网页元素不一样
#sl01是webelement类型，这个类中只有click()和send_keys()这两种操作，没有下拉框的操作，所以需要转换一下
Select(driver.find_element_by_id("add-new-area-select")).select_by_visible_text("辽宁省")
#implicity_wait在这里不起作用
time.sleep(2)
#第二个下拉框的动态id怎么处理，不能用动态id来选择
#用find_elements_by_class_name而不用find_element
#注意区别
#Select(driver.find_elements_by_class_name("add-new-area-select")[1]).select_by_visible_text("沈阳市")
Select(driver.find_elements_by_tag_name("select")[1]).select_by_visible_text("沈阳市")
time.sleep(2)
#Select(driver.find_elements_by_class_name("add-new-area-select")[2]).select_by_visible_text("和平区")
Select(driver.find_elements_by_tag_name("select")[2]).select_by_visible_text("和平区")

driver.find_element_by_css_selector(".add-new-name-span-2").send_keys("子午大道88号")
driver.find_element_by_name("address[zipcode]").send_keys("715100")
#driver.find_element_by_class_name("aui_state_highlight").click()


