# -*- coding: UTF-8 -*-
import re
import time
import random
import requests
from selenium import webdriver
import socket
import sys
class admin:
    session = requests.session()  # 商家用户
    login = session.post('http://mall.mengguochengzhen.cn/mgcz/system/login',
                              data={'loginName': '13971229922', 'password': 'qq74108520'})
    classify = session.get('http://mall.mengguochengzhen.cn/mgcz/admin/order/list')
    phone = re.findall('<button title="发货" class="btn btn-xs btn-success sendModal" data-phone="(.*?)"',
                       classify.text)
    orderId = re.findall(
        '<button title="发货" class="btn btn-xs btn-success sendModal" .*? data-keyId="(.*?)"',
        classify.text)
    mId = re.findall(
        'data-mId="(.*?)" data-toggle="modal" data-target="#sendModal">',
        classify.text)
    # def __init__(self,lagin):
    #     session = requests.session()# 商家用户
    #     self.login = session.post('http://mall.mengguochengzhen.cn/mgcz/system/login',
    #                                   data={'loginName':, 'password': 'qq74108520'})

        # self.name = name
        # self.score = score
    print(classify.text)
    print(phone)
    print(orderId)
    print(mId)

    login = session.post('http://mall.mengguochengzhen.cn/mgcz/admin/order/orderDelivery',
                              data={'orderId': orderId[0], 'phone':phone[0],'mId':mId[0],'backParam':'pageNO=1&pageSize=15&sort=createDate DESC&search_sellerId=80554807e17849cfa531315fec65d9eb&search_sort=createDate+DESC','sendPhone':'13971229922','expressNo':'13','companyNo':'','companyName':'快递公司名称','sendRemark':'发货备注'})
    print(login.text)
admin
