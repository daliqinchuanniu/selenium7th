#step1 打开浏览器
from selenium import webdriver
#step2 打开海盗商城网站
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome()

chrome.maximize_window()
chrome.get("http://localhost/index.php?m=user&c=public&a=login")
#step3 删除登录的target属性
chrome.execute_script('document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")')
#step4 点击登录按钮，跳转到登录界面
chrome.find_element_by_link_text("登录")

chrome.find_element_by_id("username").send_keys("shaozhen")
chrome.find_element_by_id("password").send_keys("000000")
#step6 输入密码
#ActionChains是一组动作和行为的意思
action = ActionChains(chrome)
action.send_keys(Keys.TAB).send_keys("000000").perform()
action.send_keys(Keys.ENTER).perform()

#假如说不支持回车键登录，可以定位登录按钮来登录，可以使用submit()来提交
#submit是提交表单，只能应用于form表单
#可以用任何一个元素执行submit()方法，来执行提交表单,不用非得定位到登录按钮才来提交
#其实不管是登录按钮，还是输入框，都不能执行提交submit()方法，而是通过广播机制找到他的父节点form，通过form来执行submit()方法
chrome.find_element_by_id("username").submit()

