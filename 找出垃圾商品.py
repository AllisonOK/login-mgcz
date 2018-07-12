#http://mall.mengguochengzhen.cn/mgcz/mobi/promotion/getPromotionCommodity?promotionId=32694c26639d484fa032bcdb3b45e114&pageNO=5
import requests
import json
# 0620ec0ec03440dcb3fc2b1b5d203fab
# 80e4884ebd9342a18979215321e822e8
# 80e4884ebd9342a18979215321e822e8
# 0620ec0ec03440dcb3fc2b1b5d203fab
# 7e0a8dbf4ceb4bae8c8fd1a0081eb352
# 7e0a8dbf4ceb4bae8c8fd1a0081eb352
# 6c814cea136449859f2793d3659e0a23
# 7e0a8dbf4ceb4bae8c8fd1a0081eb352
# 80e4884ebd9342a18979215321e822e8
# 80e4884ebd9342a18979215321e822e8
# 7e0a8dbf4ceb4bae8c8fd1a0081eb352
# 6c814cea136449859f2793d3659e0a23
# 61aca34b893d454b9b3943410f18562f
# 80e4884ebd9342a18979215321e822e8
# 7e0a8dbf4ceb4bae8c8fd1a0081eb352
# 0620ec0ec03440dcb3fc2b1b5d203fab
# 80e4884ebd9342a18979215321e822e8
# 7c208465238b40dfbaaf1e96105c3dfd
# 80e4884ebd9342a18979215321e822e8
# 05075f5627d54fe0b02a27b7df817765
# 80e4884ebd9342a18979215321e822e8
# 0620ec0ec03440dcb3fc2b1b5d203fab
# 7e0a8dbf4ceb4bae8c8fd1a0081eb352
# 6c814cea136449859f2793d3659e0a23
# 7c208465238b40dfbaaf1e96105c3dfd
# 05a1c11d9f5e4915ade964786a0f036b

# 7e0a8dbf4ceb4bae8c8fd1a0081eb352
#http://mall.mengguochengzhen.cn/mgcz/mobi/promotion/getPromotionCommodity?promotionId=c799a35fccc0453fa039aa2bd82def64&pageNO=1 //限量
#http://mall.mengguochengzhen.cn/mgcz/mobi/promotion/getPromotionCommodity?promotionId=2405cd17ea724f798f2bcdaf048fa28b&pageNO=1//品牌
#http://mall.mengguochengzhen.cn/mgcz/mobi/promotion/getPromotionCommodity?promotionId=38caa7cf51dc4e43929bdef5fb580803&pageNO=1//超市
#http://mall.mengguochengzhen.cn/mgcz/mobi/promotion/getPromotionCommodity?promotionId=c75431341c8c4e25ab7cc5205ef6a2a9&pageNO=1//会员
#http://mall.mengguochengzhen.cn/mgcz/mobi/promotion/getPromotionCommodity?promotionId=32694c26639d484fa032bcdb3b45e114&pageNO=1//每日
#f8967ee39b0a46a0ade1839667273729

list=['/promotion/getPromotionCommodity?promotionId=c799a35fccc0453fa039aa2bd82def64&pageNO=','/promotion/getPromotionCommodity?promotionId=2405cd17ea724f798f2bcdaf048fa28b&pageNO=','/promotion/getPromotionCommodity?promotionId=38caa7cf51dc4e43929bdef5fb580803&pageNO='
      '/promotion/getPromotionCommodity?promotionId=c75431341c8c4e25ab7cc5205ef6a2a9&pageNO=','/promotion/getPromotionCommodity?promotionId=32694c26639d484fa032bcdb3b45e114&pageNO=',
'f8967ee39b0a46a0ade1839667273729',


      ]
def huodong():
    for page in range(20):

        page1 = (page + 1).__str__()
        url1 = url + page1
        try:
            req = requests.post(url1)
            status = json.loads(req.text)
            status1 = status['status']
        except:
            continue

        if status1 == 0:
            break
        else:
            for i in range(30):
                try:
                    status2 = status["data"]['data'][i]['commodityPrices']
                    c = status["data"]['data'][i]["cname"]
                except:
                    break
                else:
                    if status2 == []:
                        print(c)

for k in list:
    b = k.find('promotion')
    if b !=-1:
        url = 'http://mall.mengguochengzhen.cn/mgcz/mobi'+k
        huodong()
    else:
        url = 'http://mall.mengguochengzhen.cn/mgcz/mobi/commodity/search?pageNO=1&secondary='+k
        for page in range(20):

            page1 = (page + 1).__str__()

            url = url.replace(page1,page1,1)
            print(url)

            req = requests.post(url)
            status = json.loads(req.text)
            status1 = status['status']
            if status1 == 0:
                break
            else:
                for i in range(30):
                    try:
                        status2 = status["data"]['data'][i]['commodityPrices']
                        c = status["data"]['data'][0]["cname"]
                    except:
                        break
                    else:
                        if status2 == []:
                            print(c)







# req = requests.post('http://mall.mengguochengzhen.cn/mgcz/mobi/promotion/getPromotionCommodity?promotionId=32694c26639d484fa032bcdb3b45e114&pageNO='+page)
# new_data = json.loads(req.text)
# secret_key = new_data["data"]['data'][0]['commodityPrices']
# access_token = new_data["data"]['data'][1]['commodityPrices']
# c = new_data["data"]['data'][0]["cname"]
# if secret_key ==[]:
#     print(c)
# else:
#     print('2')
# print(req.text)
# print(secret_key)
# print(access_token)