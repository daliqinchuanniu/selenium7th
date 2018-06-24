# encoding = utf-8
import unittest
import os


class TestDemo(unittest.TestCase):

    def test_KillThread(self):
        returnCode = os.system("taskkill /f /IM Xshell.exe")

        self.assertFalse(returnCode, u"结束xshell进程失败")


if __name__ == '__main__':
    unittest.main()
