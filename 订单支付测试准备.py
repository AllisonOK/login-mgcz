# -*- coding: UTF-8 -*-
import re
import time
import random
import requests
from selenium import webdriver
import pymysql
import openpyxl
import json

phone=18460457198


def size(cnid):
    connection = pymysql.connect(
        host="101.132.106.107",
        port=3306,
        user="lidawei",
        password="G1EoqS$7Jgf9l6!a",
        db="mgcz",
        charset="utf8")
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT specifications,sale_price FROM mgcz.commodity_price where cnId="'+listpay[1]+'" and commodity_id="'+listpay[0]+'"'
            cout = cursor.execute(sql)
            results = cursor.fetchall()
            size_name= results[0][0]
            sale_price = results[0][1]

            return size_name,sale_price
            connection.commit()
    finally:
        connection.close()



def pay():
    connection = pymysql.connect(
        host="101.132.106.107",
        port=3306,
        user="lidawei",
        password="G1EoqS$7Jgf9l6!a",
        db="mgcz",
        charset="utf8")
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT cId,cnId,sellerId,isPromotion,promotionId,commodity_discount FROM mgcz.commodity where sale_price <55 and state =1 order     by     rand()     limit     1 '
            cout = cursor.execute(sql)
            results = cursor.fetchall()

            cId= results[0][0]
            cnId = results[0][1]
            sellerId = results[0][2]
            isPromotion = results[0][3]
            promotionId = results[0][4]
            commodity_discount = results[0][5]
            return cId,cnId,sellerId,isPromotion,promotionId,commodity_discount
            connection.commit()
    finally:
        connection.close()



def maId(mid):
    connection = pymysql.connect(
        host="101.132.106.107",
        port=3306,
        user="lidawei",
        password="G1EoqS$7Jgf9l6!a",
        db="mgcz",
        charset="utf8")
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT maId FROM mgcz.member_addr where mId="'+str(mid)+'"'
            cout = cursor.execute(sql)
            results = cursor.fetchall()
            if cout==1:
                results1 = str(results)
            else:
                results1 = str(results[0])
            print(results1.strip("(',)"))
            return results1.strip("(',)")
            connection.commit()
    finally:
        connection.close()




se =requests.session()
#登陆
date_login = json.dumps({'password':'888888','agreement':'1','mobile':phone,'area_code':'+86'})
headers={'Host':'mall.mengguochengzhen.cn','Content-Type':'application/json; charset=utf-8','Connection':'keep-alive','Proxy-Connection':'keep-alive','Accept':'application/json','User-Agent':'mgcz/2.5.1 (iPhone; iOS 11.2.6; Scale/2.00)','Accept-Language':'zh-Hans-CN;q=1','Content-Length':'82','Accept-Encoding':'gzip, deflate'}
login=se.post('http://mall.mengguochengzhen.cn/mgcz/mobi/rpcmg/login?client_system=11.2.6&client_version=2.5.1&equipment_type=1&mac_address=02%3A00%3A00%3A00%3A00%3A00',data=date_login,headers=headers)
print(login.text)
k=json.loads(login.text)
k=k['mId']
# #新增地址
add_dizhi=se.post('http://mall.mengguochengzhen.cn/mgcz/mobi/memberAddr/save?',data={'address':'usually',
'phone':'13971229922',
'country':'东城区',
'city':'市辖区',
'town':'东华门街道',
'consignee':'luo',
'provinceCode':'11',
'cityCode':'1101',
'countryCode':'110101',
'townCode':'110101001',
'province':'北京市',
'mId':k})
print(add_dizhi.text)

maId(k)
mid_index =se.post('http://mall.mengguochengzhen.cn/mgcz//mobi/redEnvelope/askTransactionFlowing?',data={'mId':k})
print(mid_index.text)




#购买商品
# k2=json.dumps({'mId':k,
# 'cId':listpay[0],
# 'maId':maId(k),
# 'cnId':listpay[1],
# 'number':1,
# 'sellerId':listpay[2],
# 'payWay':2,
# 'discount':listpay[5],
#
# 'size':size(listpay[1]),
# 'isPromotion':listpay[3],
# 'promotionId':listpay[4],
# 'orderType':1,
# 'payDiscount':0})
# print(k2)
listpay = pay()
payDiscount=int(float(size(listpay[1])[1]-0.01)*100)

buyG1=se.post('http://mall.mengguochengzhen.cn/mgcz/mobi/order/buyNow?',data={'mId':k,
'cId':listpay[0],
'maId':maId(k),
'cnId':listpay[1],
'number':1,
'sellerId':listpay[2],
'payWay':2,
'discount':listpay[5],
'size':size(listpay[1])[0],
'isPromotion':listpay[3],
'promotionId':listpay[4],
'orderType':1,
'payDiscount':1000})

print(buyG1.text)
rrr=json.loads(buyG1.text)
orderNO=rrr['data']['orderNO']
payPrice=rrr['data']['payPrice']
#支付订单
def seller_uid(sellerId):
    connection = pymysql.connect(
        host="101.132.106.107",
        port=3306,
        user="lidawei",
        password="G1EoqS$7Jgf9l6!a",
        db="mgcz",
        charset="utf8")
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT seller_uid FROM mgcz.seller where sellerId="'+sellerId+'"'
            cout = cursor.execute(sql)
            results = cursor.fetchall()
            return str(results).strip("(',)")
            connection.commit()
    finally:
        connection.close()

def suceess(eller_uid,orderNO):
    connection = pymysql.connect(
        host="101.132.106.107",
        port=3306,
        user="lidawei",
        password="G1EoqS$7Jgf9l6!a",
        db="mgcz",
        charset="utf8")
    try:
        with connection.cursor() as cursor:
            sql = 'update order_basics set  paymentNO="0000000000",pay_type=1,order_state=1,pay_time="2018-06-14 16:56:10",seller_uid="'+eller_uid+'" where orderNO="'+orderNO+'"'
            cout = cursor.execute(sql)
            results = cursor.fetchall()
            connection.commit()
    finally:
        connection.close()

suceess(seller_uid(listpay[2]),orderNO)

#发货
# admin = requests.session()
# longin =admin.post('http://mall.mengguochengzhen.cn/mgcz/system/login',data={'loginName':'测试','password':'123123'})
# def sendx(orderNO):
#     connection = pymysql.connect(
#         host="101.132.106.107",
#         port=3306,
#         user="lidawei",
#         password="G1EoqS$7Jgf9l6!a",
#         db="mgcz",
#         charset="utf8")
#     try:
#         with connection.cursor() as cursor:
#             sql = 'SELECT orderId FROM mgcz.order_basics where orderNO="'+orderNO+'"'
#             cout = cursor.execute(sql)
#             results = cursor.fetchall()
#             return str(results).strip("(',)")
#             connection.commit()
#     finally:
#         connection.close()
# fahuo = admin.post('http://mall.mengguochengzhen.cn/mgcz/admin/order/orderDelivery',data={'orderId':sendx(orderNO),
# 'phone':'18893468510',
# 'mId':'1ea2eb6e756c4bde9fa19475eaa0f2c0',
# 'backParam':'pageNO=1&pageSize=15&sort=createDate DESC&search_sort=createDate+DESC',
# 'sendPhone':'13971229922',
# 'expressNo':'快递单号:',
# 'companyNo':'',
# 'companyName':'梦果成真有限公司',
# 'sendRemark':'备注'})
# print(longin.text)
# print(fahuo.text)