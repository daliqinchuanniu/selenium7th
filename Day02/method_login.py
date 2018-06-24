from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

# 0、打开浏览器，并最大化，并设置隐式等待时间

# 登录功能经常用到，所以是否可以把登录功能封装为一个方法，以便经常调用
# python中类的关键字也是calss
# python中方法也有一个关键字def，是define的缩写，表示定义方法。
# 方法不是一定得要定义到class中，跟java中一样
# pyton使用冒号代替大括号
class Login:
    #(self)表示类本身，类似于java的this,self参数后面详细讲
    def loginWithDefaultUser(self, driver):
        #这样登录功能就封装在 loginWithDefaultUser方法中，以后用到登录调用就可以了。

        #1、登录海盗商城；
        driver.get("http://localhost/index.php")
        driver.execute_script('document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")')
        #2、登录个人中心，点击账号设置；
        driver.find_element_by_link_text("登录").click()
        driver.find_element_by_id("username").send_keys("shaozhen")
        action = ActionChains(driver)
        action.send_keys(Keys.TAB).send_keys("000000").perform()
        driver.find_element_by_id("username").submit()