# encoding = utf-8
"""
这个文件是用来批量执行unittest测试用例的，是我们测试工具的唯一入口.
步骤：
1、导入unittest
2、指定批量执行的测试用例范围，指定的必须是继承unittest.TestCase的类。用到unittest.defaultTestLoader.discover()
3、unittest.TextTestRunner().run()批量执行 suite，生成的是文本形式的测试结果
4、HTMLTestRunner则生成的是HTML网页形式的测试报告，但是需要指令报告的路径.
    生成HTML测试报告步骤：
    A、指定报告的路径
    B、创建测试文件
    C、HTMLTestRunner().run()执行
5、发送邮件，前提条件：
    准备两个邮箱
    版本控制的前提条件是申请一个git账号，并且邮箱激活  daliqinchuanniu &daliqinchuanniu@163.com & 198688ABc#*
"""
import smtplib
import unittest
import os
from email.mime.text import MIMEText
from package.HTMLTestRunner import HTMLTestRunner


def send_mail(path):
    s_file = open(path, 'rb')  # 因为HTML文件不是文本格式，所以需要用二进制打开
    msg = s_file.read()
    mime = MIMEText(msg, _subtype='html', _charset='utf-8')
    # subtype：邮件类型，一般有三种：纯文本plain,html,富文本
    mime['Subject'] = '邵氏集团首例自动化测试报告'
    mime['From'] = 'bwftest126@126.com'
    mime['To'] = 'daliqinchuanniu@163.com'

    smtp = smtplib.SMTP()  # 实现SMTP()构造方法
    smtp.connect('smtp.126.com')  # 输入邮箱服务器地址
    smtp.login('bwftest126@126.com', 'abc123asd654')  # 只需要输入两个参数，用户名，密码
    smtp.send_message(mime, from_addr='bwftest126@126.com', to_addrs='daliqinchuanniu@163.com')
    smtp.quit()


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('./Day05', pattern='login*.py')
    #unittest.TextTestRunner().run(suite)
    ##   生成的是文本形式的测试结果
    basepath = os.path.dirname(__file__)
    f_path = basepath + '/report/test_report.html'
    file = open(f_path, 'wb')
    HTMLTestRunner(stream=file, verbosity=1, title="博为峰测试报告", description="测试环境").run(suite)

    send_mail(f_path)