from Day02.method_login import Login
#包名,文件名，类名，变量名，所有命名必须以字母开头，组成规则可以有下划线
from selenium import webdriver
import time

haidao = webdriver.Chrome()
haidao.maximize_window()
haidao.implicitly_wait(30)
#implicitly_wait()对浏览器上所有的代码都有效，每次创建浏览器，固定只写一次
#主要用于检测页面的加载时间，什么时候加载完，什么时候执行后续的程序
Login().loginWithDefaultUser(haidao)
#实例化对象之后会占用内存，Pycharm会自动帮助我们释放析构函数，释放内存
#代码运行完，检测到Login()这个对象不再被使用，系统自动释放内存

#3、点击个人资料
haidao.find_element_by_link_text("账号设置").click()
#寻找“个人资料”是否可以用find_element_by_class()来定位
#haidao.find_element_by_link_text("个人资料").click()
#当链接文本过长时，推荐使用partial_link_text方法
haidao.find_element_by_partial_link_text("个人资料").click()
#4、修改真实姓名
haidao.find_element_by_id("true_name").clear()
haidao.find_element_by_id("true_name").send_keys("秦川牛")
#5、修改性别
#xpath方法几乎可以定位所有的元素，但是可读性比较差，查询速度也比较慢，有些小浏览器对xpath的支持也不太好，不建议使用。
#haidao.find_element_by_xpath("//input[@value='1']").click()
#css定位也可以定位几乎所有的元素，所以一般建议使用css定位
#所有前端开发都会用css,利于沟通
#haidao.find_element_by_css_selector("input[value='2']").click()
#定位性别的时候，复制xpath值也定位不了，就需要xpath加工一下
haidao.find_elements_by_id("xb")[2].click()

#6、修改生日
#单独选年，选月，选日可以实现，但是稳定性比较差，并且很难修改日期，比如写完1990年2月2日，下次想换个日期就比较困难
#注意到是个文本输入框，可以使用输入框的send_keys()方法
#但是又有readonly，所以需要用JS去掉readonly属性，再用send_keys来输入
haidao.execute_script('document.getElementById("date").removeAttribute("readonly")')
haidao.find_element_by_id("date").clear()
haidao.find_element_by_id("date").send_keys("2018-03-15")
haidao.find_element_by_id("qq").clear()
haidao.find_element_by_id("qq").send_keys("6251428995")
haidao.find_element_by_css_selector("input[value='确认']").click()
time.sleep(3)
haidao.switch_to.alert.accept()
#7、修改QQ号码
#8、点击确定

