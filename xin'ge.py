# -*- coding:utf-8 -*-
'''
jpg登录测试，分下面几种情况：
(1)用户名、密码正确
(2)用户名正确、密码不正确
(3)用户名正确、密码为空
(4)用户名错误、密码正确
(5)用户名为空、密码正确
（还有其他情况，如无权限用户，被锁定用户等，就不出来了）
'''
'''
加入需要的python库:
unittest为python的测试框架
webdriver为python的selenium下的库
sleep为睡眠时间，类似于lr的思考时间，页面停留，也可以直接写import time，但是用法就是time.sleep()
os是为了创建目录time获取日期和时间
'''
import unittest
from selenium import webdriver
from time import sleep
from HTMLTestRunner import HTMLTestRunner
import os
import time
import requests
import json
# 定义打开浏览器的方法，这里用的是Chrome，火狐为Firfox，IE为Ie，必须在根目录下对应的driver才能调


# 创建测试类LoginCase，用unittest的测试框架的格式
class LoginCase(unittest.TestCase):

    # 定义登录方法，被测试用例调用
    def setUp(self):
        # 需要测试的网页
        self.url = 'http://mall.mengguochengzhen.cn/mgcz/mobi/promotion/getPromotionCommodity?promotionId=32694c26639d484fa032bcdb3b45e114&pageNO=5'



        # 定义测试方法，框架中测试方法以test_开头，底下引号中的中文会在报告中显示，利于清楚的知道测试目的

    def test_login_success(self):
        '''用户名、密码正确'''

        r = requests.post(self.url)
        # 解码json格式数据
        dicts = json.loads(r.text)
        code = r.status_code
        # 对比返回值
        self.assertEqual(code, 200)
        self.assertEqual(dicts['status'], 1)

    def test_hh(self):
        '''test'''
        self.assertEqual(1,'1')

if __name__ == '__main__':
    # 导入HTMLTestRunner库，这句也可以放在脚本开头


    # 定义脚本标题，加u为了防止中文乱码

    report_title = u'登陆模块测试报告'

    # 定义脚本内容，加u为了防止中文乱码
    desc = u'博客园登陆模块测试报告详情：'

    # 定义date为日期，time为时间
    date = time.strftime("%Y%m%d")
    time = time.strftime("%Y%m%d%H%M%S")

    # 定义path为文件路径，目录级别，可根据实际情况自定义修改
    path = 'D:/Python_test/' + date + "/login/" + time + "/"

    # 定义报告文件路径和名字，路径为前面定义的path，名字为report（可自定义），格式为.html
    report_path = path + "report.html"

    # 判断是否定义的路径目录存在，不能存在则创建
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass

    # 定义一个测试容器
    testsuite = unittest.TestSuite()

    # 将测试用例添加到容器
    testsuite.addTest(LoginCase("test_login_success"))
    testsuite.addTest(LoginCase("test_hh"))

    # 将运行结果保存到report，名字为定义的路径和文件名，运行脚本
    with open(report_path, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(testsuite)

    # 关闭report，脚本结束
    report.close()
    # 关闭浏览器
