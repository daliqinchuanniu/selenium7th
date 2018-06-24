#想要用unittest框架，首先得要导包
#unittest比selenium更常用，几乎所有测试都要用，所以python集成了Unittest

import unittest
from selenium import webdriver

#1、创建一个类，用来写测试用例，这个类需要集成unittest框架中的TestCase类
#()表示继承，继承说子类完全继承父类的所有，并有所扩展
class firstUnitTest(unittest.TestCase):
    def setUp(self):
        print(1)
    def tearDown(self):
        print(2)
        #setUp(),tearDown()方法在每个执行用例的都会执行
    def test_login(self):
        #测试用例方法必须以test开始，这个是框架规定的
        print(3)
    def switch_window(self):
        #没有以test开头的就无法自动执行，只有调用到的时候才能调用
        print(4)
    def test_zhuce(self):
        self.switch_window()
    #也可以选择重写setupclass和teardownclass方法
    #@classmethod叫做装饰器，在java中叫做注解
    @classmethod
    def setUpClass(cls):
        print(5)
    @classmethod
    def tearDownClass(cls):
        print(6)
#固定写法，表示在程序运行时候，通过这句话自动判断当前文件是不是程序的入口
#如果当前文件是程序的入口，那么就会执行if子句中的内容
if __name__ == '__main__':
    #可以理解为当前文件的主函数，
    unittest.main()