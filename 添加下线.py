import requests
import json
import hashlib
import time
import random
import string

i=1
n=20
def newzhanghao(newphone):
    newphone = newphone
    oldphone = 13971229922
    i = 0
    url_login = 'http://backendtest.mengguochengzhen.cn/v1/public/login'
    url_search = 'http://backendtest.mengguochengzhen.cn/v1/member/search'
    url_issue = 'http://backendtest.mengguochengzhen.cn/v1/cdk/issue'
    url_cdk_search = 'http://backendtest.mengguochengzhen.cn/v1/cdk/search'
    parms_login = {'token': '0', 'username': 'testadmin', 'password': '111111'}
    parms_search = {'page': '1', 'limit': '10', 'token': '0', 'info': oldphone, 'type': '2'}
    session = requests.session()
    requests_login = session.post(url_login, data=parms_login)
    requests_search = session.post(url_search, data=parms_search)
    new_data = json.loads(requests_search.text)
    if new_data=={'code': 1, 'message': '查无数据'}:
       print('手机号不存在查无数据')
    else:
       account_id = new_data["data"][0]["account_id"]
       parms_issue = {'token': '0', 'cdk_grade': '1', 'number': '1', 'account_id': account_id}
       requests_issue = session.post(url_issue, parms_issue)
       parms_cdk_ID = {'page': '1', 'limit': '10', 'token': '0', 'info': oldphone, 'type': '2'}
       requests_cdk_ID = session.post(url_cdk_search, parms_cdk_ID)
       new_data2 = json.loads(requests_cdk_ID.text)
       while i < 50:
          CDK_code = new_data2["data"][i]["cdk_code"]
          status = new_data2["data"][i]["status"]
          if status != '1':
             i = i + 1
          else:
             i = 51
    # 新增一个用户
    parms_add = {'token': '0', 'area_code': '+86', 'mobile': newphone, 'referee_area_code': '+86',
             'referee_mobile': oldphone, 'account_type': '1', 'cdk_code': CDK_code}
    requests_add = session.post('http://backendtest.mengguochengzhen.cn/v1/member/add', data=parms_add)
    new_data3 = json.loads(requests_add.text)
    if  new_data3 == {'code': 1101, 'message': '此手机号已经被使用'}:
        print(new_data3)
    else:
        print(newphone+'注册成功')


def suijishu(n):
    phone_random1 = ''.join(random.sample(['1','2','3','4','5','6','7','8','9','0'], 8))
    phone_random2 = ''.join(random.sample(['139', '139', '147', '148', '152', '184', '187', '188', '178', '137'], 1))
    phone_random  = phone_random2+phone_random1
    newzhanghao(phone_random)
while i<n :
    suijishu(n)
    i=i+1
