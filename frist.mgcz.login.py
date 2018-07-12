import requests
import json
import hashlib
import time

# token_ciphertext = md5js(access_token, str_time(), secret_key)//获取token_ciphertext动态值

Mobblie = 13971229922


def md5js(access_token, ClientInfotime, secret_key):
    str = 'access_token=' + access_token + '&request_timestamp=' + ClientInfotime + '&secret_key=' + secret_key
    hl = hashlib.md5()
    hl.update(str.encode(encoding='utf-8'))
    return hl.hexdigest()


def str_time():
    return str(int(time.time()))
    # 登陆游戏


def LoginGame(Mobblie):
    url = 'http://game2test.mengguochengzhen.cn/v1/public/login?equipment_type=1&client_version=2.0.0&request_timestamp=1518086887&client_system=ios&mac_address=1'
    parms = {"password":"qq74108520","mobile":Mobblie,"area_code":"+86","agreement":"1"}
    values = json.dumps(parms)
    req = requests.post(url, data=values)
    new_data = json.loads(req.text)
    secret_key = new_data["data"]["secret_key"]
    access_token = new_data["data"]["access_token"]
    print(req.text)
    return secret_key, access_token


[secret_key, access_token] = LoginGame(Mobblie)


# 购买苹果种子
def case1():
    clientInfotime = str_time()
    secret_key1 = md5js(access_token=access_token, ClientInfotime=clientInfotime, secret_key=secret_key)
    goumai = 'http://game2test.mengguochengzhen.cn/v1/store/buy-goods?equipment_type=1&client_version=2.0.0&request_timestamp=' + clientInfotime + '&client_system=ios&mac_address=1&access_token=' + access_token + '&token_ciphertext=' + secret_key1
    parms1 = {"goods_version": "1514875211", "goods_price": "1380", "goods_id": "1", "buy_number": 1}
    values1 = json.dumps(parms1)
    req1 = requests.post(goumai, data=values1)
    new_data = json.loads(req1.text)
    message = new_data["message"]
    print('购买苹果种子:' + message)
    return message


# 购买荔枝种子
def case2():
    clientInfotime = str_time()
    secret_key1 = md5js(access_token=access_token, ClientInfotime=clientInfotime, secret_key=secret_key)
    goumai = 'http://game2test.mengguochengzhen.cn/v1/store/buy-goods?equipment_type=1&client_version=2.0.0&request_timestamp=' + clientInfotime + '&client_system=ios&mac_address=1&access_token=' + access_token + '&token_ciphertext=' + secret_key1
    parms1 = {"goods_version": "1514875211", "goods_price": "1380", "goods_id": "2", "buy_number": 1}
    values1 = json.dumps(parms1)
    req1 = requests.post(goumai, data=values1)
    new_data = json.loads(req1.text)
    message = new_data["message"]
    print('购买荔枝种子:' + message)
    return message


# 购买琵琶种子
def case3():
    clientInfotime = str_time()
    secret_key1 = md5js(access_token=access_token, ClientInfotime=clientInfotime, secret_key=secret_key)
    goumai = 'http://game2test.mengguochengzhen.cn/v1/store/buy-goods?equipment_type=1&client_version=2.0.0&request_timestamp=' + clientInfotime + '&client_system=ios&mac_address=1&access_token=' + access_token + '&token_ciphertext=' + secret_key1
    parms1 = {"goods_version": "1514875211", "goods_price": "1380", "goods_id": "3", "buy_number": 1}
    values1 = json.dumps(parms1)
    req1 = requests.post(goumai, data=values1)
    new_data = json.loads(req1.text)
    message = new_data["message"]
    print('购买琵琶种子' + message)
    return message


# 购买铁铲
def case4():
    clientInfotime = str_time()
    secret_key1 = md5js(access_token=access_token, ClientInfotime=clientInfotime, secret_key=secret_key)
    goumai = 'http://game2test.mengguochengzhen.cn/v1/store/buy-goods?equipment_type=1&client_version=2.0.0&request_timestamp=' + clientInfotime + '&client_system=ios&mac_address=1&access_token=' + access_token + '&token_ciphertext=' + secret_key1
    parms1 = {"goods_version": "1514875211", "goods_price": "20", "goods_id": "25", "buy_number": 1}
    values1 = json.dumps(parms1)
    req1 = requests.post(goumai, data=values1)
    new_data = json.loads(req1.text)
    message = new_data["message"]
    print('购买铁铲' + message)
    return message


# 购买氮肥
def case5():
    clientInfotime = str_time()
    secret_key1 = md5js(access_token=access_token, ClientInfotime=clientInfotime, secret_key=secret_key)
    goumai = 'http://game2test.mengguochengzhen.cn/v1/store/buy-goods?equipment_type=1&client_version=2.0.0&request_timestamp=' + clientInfotime + '&client_system=ios&mac_address=1&access_token=' + access_token + '&token_ciphertext=' + secret_key1
    parms1 = {"goods_version": "1514875211", "goods_price": "100", "goods_id": "19", "buy_number": 1}
    values1 = json.dumps(parms1)
    req1 = requests.post(goumai, data=values1)
    new_data = json.loads(req1.text)
    message = new_data["message"]
    print('购买氮肥' + message)
    return message


# 扩建土地
def case6():
    clientInfotime = str_time()
    secret_key1 = md5js(access_token=access_token, ClientInfotime=clientInfotime, secret_key=secret_key)
    goumai = ' http://game2test.mengguochengzhen.cn/v1/farm/reclamation?equipment_type=1&client_version=2.0.0&request_timestamp=' + clientInfotime + '&client_system=ios&mac_address=1&access_token=' + access_token + '&token_ciphertext=' + secret_key1
    parms1 = {"new_land_number": "2"}  # 代表第几块土地
    values1 = json.dumps(parms1)
    req1 = requests.post(goumai, data=values1)
    new_data = json.loads(req1.text)
    message = new_data["message"]
    print('扩建土地' + message)
    return message


# 开垦土地
def case7():
    clientInfotime = str_time()
    secret_key1 = md5js(access_token=access_token, ClientInfotime=clientInfotime, secret_key=secret_key)
    goumai = 'http://game2test.mengguochengzhen.cn/v1/farm/fertilization?equipment_type=1&client_version=2.0.0&request_timestamp=' + clientInfotime + '&client_system=ios&mac_address=1&access_token=' + access_token + '&token_ciphertext=' + secret_key1
    parms1 = {"land_number": "1"}  # 代表第几块土地
    values1 = json.dumps(parms1)
    req1 = requests.post(goumai, data=values1)
    new_data = json.loads(req1.text)
    message = new_data["message"]
    print('开垦土地：' + message)
    return message


# 播种
def case8():
    clientInfotime = str_time()
    secret_key1 = md5js(access_token=access_token, ClientInfotime=clientInfotime, secret_key=secret_key)
    goumai = 'http://game2test.mengguochengzhen.cn/v1/farm/planting?equipment_type=1&client_version=2.0.0&request_timestamp=' + clientInfotime + '&client_system=ios&mac_address=1&access_token=' + access_token + '&token_ciphertext=' + secret_key1
    parms1 = {"warehouse_id": "48", "land_number": "1", "goods_id": "1"}  # 播种种子
    values1 = json.dumps(parms1)
    req1 = requests.post(goumai, data=values1)
    new_data = json.loads(req1.text)
    message = new_data["message"]
    print('播种：' + message)
    return message


# 施肥
def case9():
    clientInfotime = str_time()
    secret_key1 = md5js(access_token=access_token, ClientInfotime=clientInfotime, secret_key=secret_key)
    goumai = 'http://game2test.mengguochengzhen.cn/v1/farm/fertilization?equipment_type=1&client_version=2.0.0&request_timestamp=' + clientInfotime + '&client_system=ios&mac_address=1&access_token=' + access_token + '&token_ciphertext=' + secret_key1
    parms1 = {"land_number": "1"}  # 施肥
    values1 = json.dumps(parms1)
    req1 = requests.post(goumai, data=values1)
    new_data = json.loads(req1.text)
    message = new_data["message"]
    print('施肥' + message)
    return message


if case7() == 'SUCCESS':
    if case8() == 'SUCCESS':
        if case9() == 'SUCCESS':
            print(' \n')
        else:
            case5()
            case9()
    else:
        case1()
        if case9() == 'SUCCESS':
            print('\n')
        else:
            case5()
            case9()
else:
    case4()
    if case8() == 'SUCCESS':
        if case9() == 'SUCCESS':
            print('\n')
        else:
            case5()
            case9()
    else:
        case1()
        if case9() == 'SUCCESS':
            print('\n')
        else:
            case5()
            case9()
