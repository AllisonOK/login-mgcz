# -*- coding: UTF-8 -*-
import re
import time
import random
import requests
from selenium import webdriver
import pymysql
import openpyxl
import json
phone_random1 = ''.join(random.sample(['1','2','3','4','5','6','7','8','9','0'], 8))
phone_random2 = ''.join(random.sample(['139', '139', '147', '148', '152', '184', '187', '188', '178', '137'], 1))
phone_random  = phone_random2+phone_random1
def sms_code(phone):
    connection = pymysql.connect(
        host="101.132.106.107",
        port=3306,
        user="lidawei",
        password="G1EoqS$7Jgf9l6!a",
        db="mgcz",
        charset="utf8")
    try:

        with connection.cursor() as cursor:
            sql = 'SELECT verification_code FROM mgcz_ucenter.uc_sms_verification where status=1 and mobile=' + str(phone)
            cout = cursor.execute(sql)
            results = cursor.fetchall()
            results1 = str(results)
            print(results1.strip("(',)"))
            return results1.strip("(',)")
            connection.commit()

    finally:

        connection.close()

def cdk_code():
    connection = pymysql.connect(
        host="101.132.106.107",

        port=3306,

        user="lidawei",

        password="G1EoqS$7Jgf9l6!a",

        db="mgcz_ucenter",

        charset="utf8")

    try:

        with connection.cursor() as cursor:
            sql = 'SELECT data from uc_gcode WHERE uid =0 and datetime=0  LIMIT 1'
            cout = cursor.execute(sql)
            results = cursor.fetchall()
            results1 = str(results)
            print(results1.strip("(',)"))
            return results1.strip("(',)")
            connection.commit()

    finally:

        connection.close()

print(phone_random)
da1 = json.dumps({"sms_type":1,"mobile":phone_random,"area_code":"+86"})
re  = requests.post('http://game2test.mengguochengzhen.cn/v1/public/send-sms-verify?equipment_type=1&client_version=2.0.0&request_timestamp='+str(int(time.time()))+'&client_system=windows&mac_address=1&access_token=null&token_ciphertext=29bafa77b1a38c763c634b6a84047215',data=da1)
print(re.text)
da2 = json.dumps({"sms_code":sms_code(phone_random),"mobile":phone_random,"cdk_code":cdk_code(),"area_code":"+86"})
rek =requests.post('http://game2test.mengguochengzhen.cn/v1/public/register?equipment_type=1&client_version=2.0.0&request_timestamp='+str(int(time.time()))+'&client_system=windows&mac_address=1',data=da2)
print(rek.text)

# da3 = requests.post('http://dream2test.mengguochengzhen.cn/activate-history/callback',)
se =requests.session()

#登陆
date_login = json.dumps({'password':'888888','agreement':'1','mobile':phone_random,'area_code':'+86'})
headers={'Host':'mall.mengguochengzhen.cn','Content-Type':'application/json; charset=utf-8','Connection':'keep-alive','Proxy-Connection':'keep-alive','Accept':'application/json','User-Agent':'mgcz/2.5.1 (iPhone; iOS 11.2.6; Scale/2.00)','Accept-Language':'zh-Hans-CN;q=1','Content-Length':'82','Accept-Encoding':'gzip, deflate'}
#login=se.post('http://mall.mengguochengzhen.cn/mgcz/mobi/rpcmg/login?client_system=11.2.6&client_version=2.5.1&equipment_type=1&mac_address=02%3A00%3A00%3A00%3A00%3A00',data=date_login,headers=headers)
login1=se.post('http://mall.mengguochengzhen.cn/mgcz/mobi/rpcmg/login?client_system=11.2.6&client_version=2.5.1&equipment_type=1&mac_address=02%3A00%3A00%3A00%3A00%3A00',data=date_login,headers=headers)
print(login1.text)
k=json.loads(login1.text)
print(k['data']['token_data']['uid'])
k=k['mId']

mid_index =se.post('http://mall.mengguochengzhen.cn/mgcz/mobi/redEnvelope/askTransactionFlowing?',data={'mId':k})
print(mid_index.text)
