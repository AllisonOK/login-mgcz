import json

import requests

phone = 15227513690
    # 修改的手机号码
gold_amount = 999999      # 金币数量
max_quota = 690000.00    # 最大使用额度

url_login = 'http://backendtest.mengguochengzhen.cn/v1/public/login'
url_search = 'http://backendtest.mengguochengzhen.cn/v1/member/search'
url_issue = 'http://backendtest.mengguochengzhen.cn/v1/cdk/issue'
url_cdk_search = 'http://backendtest.mengguochengzhen.cn/v1/cdk/search'
parms_login = {'token': '0', 'username': 'testadmin', 'password': '111111'}
parms_search = {'page': '1', 'limit': '10', 'token': '0', 'info': phone, 'type': '2'}
session = requests.session()
requests_login = session.post(url_login, data=parms_login)
requests_search = session.post(url_search, data=parms_search)

new_data = json.loads(requests_search.text)
account_id = new_data["data"][0]["account_id"]

# 增加金币
parms_add_gold = {'token': '0', 'account_id': account_id, 'area_id': '+86', 'mobile': phone, 'real_name': 'luozhihao',
                  'identity_card': '420984199512087839', 'nickname': '梦果', 'gold_amount': gold_amount,
                  'commission_amount': '999', 'love_number': '99', 'use_quota': 0, 'max_quota': max_quota,
                  'cdk_code': '', 'rounds_number': 1, 'is_service_charge': 1}
requests_add_gold = session.post('http://backendtest.mengguochengzhen.cn/v1/member/edit', data=parms_add_gold)
print(requests_add_gold.text)
