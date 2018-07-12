#encoding=utf8
import sys
import getopt
import time
import re
from selenium import webdriver
import requests
import json
import  openpyxl
import codecs
import pymysql
url = 'http://mall.mengguochengzhen.cn'
driver = webdriver.Chrome()
driver.get(url+'/mgcz/system/index')
driver.find_element_by_id('form-username').send_keys('root')
driver.find_element_by_id('form-password').send_keys('123123')
driver.find_element_by_xpath('//*[@id="login-form"]/button').click()
time.sleep(5) #拿登陆后的最新cookies
# 获取cookie信息
cookies = driver.get_cookies()

sid=cookies[1]['value']
JSESSIONID=cookies[0]['value']

def sjk(sql):

    connection = pymysql.connect(
        host="101.132.106.107",
        port=3306,
        user="lidawei",
        password="G1EoqS$7Jgf9l6!a",
        db="mgcz",
        charset="utf8")
    try:
        with connection.cursor() as cursor:

            cout = cursor.execute(sql)
            results = cursor.fetchall()
            results1 = str(results)
            print(results1.strip("(',)"))
            return results1.strip("(',)")
            connection.commit()
    finally:

        connection.close()


for i in range(0,31):
    vv=sjk('SELECT cId FROM mgcz.commodity where state=1 and isPromotion = 0  order     by     rand()     limit     1  ')

    re1=requests.post('http://mall.mengguochengzhen.cn/mgcz/admin/promotion/savePromotionCommodity',data={'promotionId':'a879a3f653d24adfbeea8c06dad66d63','cId':str(vv),'isCommit':'1','commodityDiscount':'10'},headers={'Cookie': 'JSESSIONID=' + JSESSIONID + '; sid=' + sid})
    print(re1.text)
    v1=sjk('SELECT pc_id FROM mgcz.promotion_commodity where promotion_id="a879a3f653d24adfbeea8c06dad66d63"and cId="'+vv+'"')
    re5 =requests.post('http://mall.mengguochengzhen.cn/mgcz/admin/promotion/updateAuditingState',data={'promotionId':'a879a3f653d24adfbeea8c06dad66d63','pcId':str(v1),'cId':str(vv),'discount':'1.00','auditingState':1,'sort':'a.create_date DESC'},headers={'Cookie': 'JSESSIONID=' + JSESSIONID + '; sid=' + sid})
    print(re5.text)