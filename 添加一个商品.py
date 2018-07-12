# -*- coding: UTF-8 -*-
import re
import time
import random
import requests
from selenium import webdriver


driver = webdriver.Chrome()
# driver.get("http://member.rltxtest.xyz/login/login.html")
driver.get("http://mall.mengguochengzhen.cn/mgcz/system/index")


driver.find_element_by_id('form-username').send_keys('13971229922')
driver.find_element_by_id('form-password').send_keys('qq74108520')
driver.find_element_by_xpath('//*[@id="login-form"]/button').click()
time.sleep(5) #拿登陆后的最新cookies

# 获取cookie信息
cookies = driver.get_cookies()
print(cookies)
sid=cookies[1]['value']
JSESSIONID=cookies[0]['value']
cookie ='sid='+sid+";"+'JSESSIONID='+JSESSIONID

# 打印获取的cookies信息

salePrice = random.randint(0,99)
gamePrice = 2
requirePrice = salePrice-4
accountPrice =salePrice-gamePrice


cname = ' 商品名称'  # 商品名称
gcode = '12134560'  # 商品编码
stock = '1321'  # 库存

firstClassify = 'e5ec0199df8a4d0f806f3224a2ef9f11'  # 一级分类
secondClassify = '6f6d2fc8d70242d5bf231a45ae4a9331'  # 二级分类
describes = '<span style="color:#393939;font-family:微软雅黑;font-size:14px;background-color:#FFFFFF;">商品详情</span>'
img = '/mgcz/upload/kindeditor/image/20180403/20180403093311_997.jpg'
url_save = 'http://mall.mengguochengzhen.cn/mgcz/admin/commodity/save'
# ---------------------------------------------------规格-------------------------------
sizeName = '1'  # 规格名称
sizeValue = '1'  # 规格属性

data1={'cname': cname, 'gcode': gcode, 'stock': stock, 'firstClassify': firstClassify,
                                   'secondClassify': secondClassify, 'describes': describes}

session = requests.session()  # 商家用户

session_admin = requests.session()  # 总管理员



# 商家添加商品
requests_save = session.post(url_save,
                             data={'img':'','cname': cname, 'gcode': gcode, 'stock': stock, 'firstClassify': firstClassify,
                                   'secondClassify': secondClassify, 'describes': describes},headers={'Cookie':'JSESSIONID='+JSESSIONID+'; sid='+sid})
print(requests_save.text)
#设置规格
requests_login111 = session.get('http://mall.mengguochengzhen.cn/mgcz/admin/commodity',headers={'Cookie':'JSESSIONID='+JSESSIONID+'; sid='+sid})
# requests_addNorms = session.post('http://mall.mengguochengzhen.cn/mgcz/admin/commodityNorms/addNorms ',
#                                  data={'sellerId': '80554807e17849cfa531315fec65d9eb', 'sizeName': sizeName,
#                                        'sizeValue': sizeValue, 'normsState': 1})
# print(requests_addNorms.text)

res_tr = re.compile('<input type="radio" name="cnId"  value="(.*?)">')
match = res_tr.findall(requests_login111.text)
for line in match:
    print(line)
sizeName = re.findall('<input type="hidden" name="sizeName" value="(.*?)">',requests_login111.text)
# specifications = re.findall('<button title="编辑" class="btn btn-xs btn-primary edit" data-keyId="(.*?)">',requests_login111.text)
Cid = re.findall('<button title="编辑" class="btn btn-xs btn-primary edit" data-keyId="(.*?)"',requests_login111.text)
for line1 in Cid:
    print(line1)






request_set_specifications = session.post('http://mall.mengguochengzhen.cn/mgcz/admin/commodity/bindingNorms',data={'cnId':match[0],'cId':Cid[0]},headers={'Cookie':'JSESSIONID='+JSESSIONID+'; sid='+sid})
# print(request_set_specifications.text)

request_init_editPrice = session.post('http://mall.mengguochengzhen.cn/mgcz/admin/commodity/init_editPrice',data={'cId':Cid[0],'backParam':'pageNO=1&pageSize=15&sort=a.create_date DESC&search_sort=a.create_date+DESC'},)

specifications = re.findall('<label><input type="radio" name="sizeVlue"  value="(.*?)"',request_init_editPrice.text)
for line2 in specifications:
    print(line2)
    requests_saveCommodityPrice = session.post('http://mall.mengguochengzhen.cn/mgcz/admin/commodity/saveCommodityPrice',data={'sizeName':sizeName[0],'specifications':line2,'commodityId':Cid[0],'salePrice':salePrice,'gamePrice':gamePrice,'requirePrice':requirePrice,'accountPrice':accountPrice,'stock':0},headers={'Cookie':'JSESSIONID='+JSESSIONID+'; sid='+sid})
# 总管理员登陆登陆
# requests_login = session_admin.post('http://mall.mengguochengzhen.cn/mgcz/system/login',
#                               data={'loginName':'admin','password':'123123'})

requests_k = session.post('http://mall.mengguochengzhen.cn/mgcz/admin/commodity/editState',data={'cId':Cid[0],'state':1,'backParam':'pageNO=1&pageSize=15&sort=a.create_date DESC&search_sort=a.create_date+DESC'})