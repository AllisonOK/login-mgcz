# -*- coding: UTF-8 -*-
import re
import time
import random
import requests
import json
headers = {'Host':'mall.mengguochengzhen.cn',
'Content-Type':'application/json; charset=utf-8',
'Connection':'keep-alive',
'Proxy-Connection':'keep-alive',
'Accept':'application/json',
'User-Agent':'mgcz/2.5.1 (iPhone; iOS 11.2.6; Scale/2.00)',
'Accept-Language':'zh-Hans-CN;q=1',
'Content-Length':'82',
'Accept-Encoding':'gzip, deflate'
}

d = {'password':'qq741085220','agreement':'1','mobile':'13971229922','area_code':'+86'}
data= {'client_system':'11.2.6','client_version':'2.5.1','equipment_type':1,'mac_address':'02:00:00:00:00:00'}
d1 = json.dumps(d)
r = requests.post('http://mall.mengguochengzhen.cn/mgcz/mobi/rpcmg/login?client_system=11.2.6&client_version=2.5.1&equipment_type=1&mac_address=02%3A00%3A00%3A00%3A00%3A00',data=d1,headers=headers)
print(r.text)
d2 = json.loads(r.text)
d4 = d2['status']
print(d4)