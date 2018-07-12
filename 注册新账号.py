import requests
import json
import hashlib
import time
#
#
#
#
newphone = 13528195524
oldphone = 13971229922
i = 0
url_login = 'http://backend.mengguochengzhen.cn/v1/public/login'
url_search = 'http://backend.mengguochengzhen.cn/v1/member/search'
url_issue = 'http://backend.mengguochengzhen.cn/v1/cdk/issue'
url_cdk_search = 'http://backend.mengguochengzhen.cn/v1/cdk/search'
parms_login = {'token': '0', 'username': 'testadmin', 'password': '111111'}
parms_search = {'page': '1', 'limit': '10', 'token': '0', 'info': oldphone, 'type': '2'}
session = requests.session()
requests_login = session.post(url_login, data=parms_login)
requests_search = session.post(url_search, data=parms_search)
new_data = json.loads(requests_search.text)
if new_data=={'code': 1, 'message': '查无数据'}:
    print(new_data)
else:
    account_id = new_data["data"][0]["account_id"]
    parms_issue = {'token': '0', 'cdk_grade': '1', 'number': '1', 'account_id': account_id}
    requests_issue = session.post(url_issue, parms_issue)
    parms_cdk_ID = {'page': '1', 'limit': '10', 'token': '0', 'info': oldphone, 'type': '2'}
    requests_cdk_ID = session.post(url_cdk_search, parms_cdk_ID)
    print(requests_cdk_ID.text)
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
    requests_add = session.post('http://backend.mengguochengzhen.cn/v1/member/add', data=parms_add)
    print(requests_add.text)
    new_data3 = json.loads(requests_add.text)
    if  new_data3 == {'code': 1101, 'message': '此手机号已经被使用'}:
        print(new_data3)
    else:
        new_ID = new_data3['data']['account_id']
      # 增加金币
        parms_add_gold = {'token': '0', 'account_id': new_ID, 'area_id': '+86', 'mobile': newphone,
                      'real_name': 'luozhihao', 'identity_card': '420984199512087839', 'nickname': '梦果',
                      'gold_amount': 0, 'commission_amount': '999', 'love_number': '5', 'use_quota': 0,
                      'max_quota': 69000.00, 'cdk_code': '', 'rounds_number': 1, 'is_service_charge': 1}
        requests_add_gold = session.post('http://backendtest.mengguochengzhen.cn/v1/member/edit', data=parms_add_gold)
        print(requests_add_gold.text)
