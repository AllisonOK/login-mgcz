import requests
import json
import hashlib
import time
from multiprocessing import Pool

def LoginGame(i):
    url = 'https://backendtest.mengguochengzhen.cn'
    req = requests.post(url)
    new_data = json.loads(req.text)
    # print(req.status_code+i)
    # req1 =requests.get('http://shop.mengguochengzhen.cn/mgcz'+new_data['data'][0]['picUrl'])
    # req2 = requests.get('http://shop.mengguochengzhen.cn/mgcz' + new_data['data'][1]['picUrl'])
    # req3 = requests.get('http://shop.mengguochengzhen.cn/mgcz' + new_data['data'][2]['picUrl'])
    # req4 = requests.get('http://shop.mengguochengzhen.cn/mgcz' + new_data['data'][3]['picUrl'])
    # print('http://shop.mengguochengzhen.cn/mgcz'+new_data['data'][0]['picUrl'])
    # print('http://shop.mengguochengzhen.cn/mgcz' + new_data['data'][1]['picUrl'])
    # print('http://shop.mengguochengzhen.cn/mgcz' + new_data['data'][2]['picUrl'])
    # print('http://shop.mengguochengzhen.cn/mgcz' + new_data['data'][3]['picUrl'])

    req5 = requests.post('http://shop.mengguochengzhen.cn/mgcz/mobi/promotion/query')
    new_data1 = json.loads(req5.text)
    print(new_data1)
    print(new_data)
    # req6 = requests.get('http://shop.mengguochengzhen.cn/mgcz' + new_data1['data'][0]['promotionImg'])
    # req7 = requests.get('http://shop.mengguochengzhen.cn/mgcz' + new_data1['data'][1]['promotionImg'])
    # req8 = requests.get('http://shop.mengguochengzhen.cn/mgcz' + new_data1['data'][2]['promotionImg'])
    # req9 = requests.get('http://shop.mengguochengzhen.cn/mgcz' + new_data1['data'][3]['promotionImg'])
    # print('http://shop.mengguochengzhen.cn/mgcz' + new_data1['data'][0]['promotionImg'])
    # print('http://shop.mengguochengzhen.cn/mgcz' + new_data1['data'][1]['promotionImg'])
    # print('http://shop.mengguochengzhen.cn/mgcz' + new_data1['data'][2]['promotionImg'])
    # print('http://shop.mengguochengzhen.cn/mgcz' + new_data1['data'][3]['promotionImg'])
    # req10 = requests.post('http://shop.mengguochengzhen.cn/mgcz/mobi/commodity/hot')
LoginGame(1)
#
# def main():
#     pool = Pool(processes=200)    # set the processes max number 3
#     for i in range(1,2000):
#         pool.apply_async(LoginGame(i), (i,))
#     pool.close()
#     pool.join()
#
#
# if __name__ == "__main__":
#     main()

