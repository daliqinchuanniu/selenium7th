# encoding = utf-8
from selenium import webdriver
import unittest
import time
import traceback


class TestDemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(10)
        self.quit()

    def test_scroll(self):
        url = "http://www.seleniumhg.org/"
        try:
            self.driver.get(url)
            #使用JS的scrollTo()和document.body.scrollHeight参数，将页面滚动到最下方
            self.driver.execute_script("window.scrollTo(100, document.body.scrollHeight);")
            time.sleep(3)
#           使用JS的scrollIntoView()将遮挡的元素滚动到可见屏幕上
            self.driver.execute_script("document.getElementById('choice').scrollIntoView(true);")
            time.sleep(3)
#           使用JS的scrollBy()使用0,400横坐标将页面向下滚动400像素
            self.driver.execute_script("window.scrollBy(0, 400);")
            time.sleep(3)

        except Exception:
            print
            traceback.print_exc()


if __name__ == '__main__':
    unittest.main()