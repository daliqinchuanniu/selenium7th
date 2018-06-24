# encoding = utf-8
import unittest
from selenium import webdriver
import time


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()

    @classmethod
    def tearDown(cls):
        time.sleep(15)
        cls.driver.quit()