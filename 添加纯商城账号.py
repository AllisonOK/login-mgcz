#http://mall.mengguochengzhen.cn/mgcz/mobi/rpcmg/sendVerify?mac_address=B0:E2:35:29:8B:60&client_system=7.0&client_version=2.5.2&equipment_type=2
import time
import requests
import json
import random
def suijishu():
    phone_random1 = ''.join(random.sample(['1','2','3','4','5','6','7','8','9','0'], 8))
    phone_random2 = ''.join(random.sample(['139', '139', '147', '148', '152', '184', '187', '188', '178', '137'], 1))
    phone_random  = phone_random2+phone_random1
    return phone_random

phone = suijishu()


dd = json.dumps({"sms_type":"1","source_ip":"10.17.36.51","mobile":phone,"area_code":"+86"})


ddd=headers = {'Host':'mall.mengguochengzhen.cn',
                        'Content-Type':'application/json; charset=utf-8',
                        'Connection':'keep-alive',
                        'Proxy-Connection':'keep-alive',
                        'Accept':'application/json',
                        'User-Agent':'mgcz/2.5.1 (iPhone; iOS 11.2.6; Scale/2.00)',
                        'Accept-Language':'zh-Hans-CN;q=1',
                        'Content-Length':'82',
                        'Accept-Encoding':'gzip, deflate'
                        }
login_success = requests.post('http://mall.mengguochengzhen.cn/mgcz/mobi/rpcmg/sendVerify?mac_address=B0:E2:35:29:8B:60&client_system=7.0&client_version=2.5.2&equipment_type=2',data=dd,headers=ddd)
print(login_success.text)

import pymysql

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


dd1 = json.dumps({"password":"888888","nickname":"罗","mobile":phone,"area_code":"+86","source_ip":"10.17.36.51","sms_code":sms_code(phone),"agreement":"1"})
login_success1 = requests.post('http://mall.mengguochengzhen.cn/mgcz/mobi/rpcmg/register?mac_address=B0:E2:35:29:8B:60&client_system=7.0&client_version=2.5.2&equipment_type=2',data=dd1,headers=ddd)
print(login_success1.text)
print(phone)
dd3 = json.dumps({'password':'888888','agreement':'1','mobile':phone,'area_code':'+86'})
s =requests.session()
denglu = s.post('http://mall.mengguochengzhen.cn/mgcz/mobi/rpcmg/login?client_system=11.2.6&client_version=2.5.1&equipment_type=1&mac_address=02%3A00%3A00%3A00%3A00%3A00',data=dd3,headers=ddd)

xdz = s.post('http://mall.mengguochengzhen.cn/mgcz/mobi/memberAddr/save?address=%E7%A9%BA&countryCode=140421&town=%E8%8D%AB%E5%9F%8E%E9%95%87&consignee=%E5%A4%AA%E5%8F%AF%E6%80%9C%E4%BA%86&country=%E9%95%BF%E6%B2%BB%E5%8E%BF&townCode=140421102&mId=7be91bb5f68a40bb9ef01089a634d490&provinceCode=14&city=%E9%95%BF%E6%B2%BB%E5%B8%82&phone=13971229922&province=%E5%B1%B1%E8%A5%BF&cityCode=1404')
print(xdz.text)
se =requests.session()
#登陆
date_login = json.dumps({'password':'888888','agreement':'1','mobile':phone,'area_code':'+86'})
headers={'Host':'mall.mengguochengzhen.cn','Content-Type':'application/json; charset=utf-8','Connection':'keep-alive','Proxy-Connection':'keep-alive','Accept':'application/json','User-Agent':'mgcz/2.5.1 (iPhone; iOS 11.2.6; Scale/2.00)','Accept-Language':'zh-Hans-CN;q=1','Content-Length':'82','Accept-Encoding':'gzip, deflate'}
login=se.post('http://mall.mengguochengzhen.cn/mgcz/mobi/rpcmg/login?client_system=11.2.6&client_version=2.5.1&equipment_type=1&mac_address=02%3A00%3A00%3A00%3A00%3A00',data=date_login,headers=headers)
print(login.text)
k=json.loads(login.text)

k=k['mId']
d = json.dumps({'address':'usually',
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
#新增地址
add_dizhi=se.post('http://mall.mengguochengzhen.cn/mgcz/mobi/memberAddr/save?',data=d,headers=headers)
print(add_dizhi.text)













# #购买会员卡订单
# k=json.loads(login.text)
# k=k['mId']
# k1=json.dumps({"mobile":phone,"area_code":"+86","sms_type":"9"})
# buyG=se.post('http://mall.mengguochengzhen.cn/mgcz/mobi/rpcmg/sendVerify?client_system=11.3.1&client_version=2.5.3&equipment_type=1&mac_address=02:00:00:00:00:00',data=k1,headers=headers)
# print(buyG.text)
# k2=json.dumps({"discount":"1","mId":k,"sellerId":"60ba2a3c18f0401aa6c7cd4931558698","cnId":"6938cd2035794d49bbdb77d8e7b6ef0b","phone":phone,"sendStatus":"0","cId":"b0a0d9d93cab4b9da9cbbd95da54156d","size":"充值卡","payWay":"2","code":sms_code(phone),"fullName":"Ki","number":"1","smsType":"9","area_code":"+86"})
# buyG1=se.post('http://mall.mengguochengzhen.cn/mgcz/mobi/memberCard/confirmNow?client_system=11.3.1&client_version=2.5.3&equipment_type=1&mac_address=02:00:00:00:00:00',data=k2,headers=headers)
# print(buyG1.text)
# G3 =se.post('http://mall.mengguochengzhen.cn/mgcz/mobi/order/orderPay?',data={'mId':k,'payType':1,'orderId':''})