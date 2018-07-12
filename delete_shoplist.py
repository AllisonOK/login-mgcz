import requests
import json
import hashlib
import time
session = requests.session()  # 商家用户

# 22b3bd8860d94ae591e3b2432bf1ba85
# 49b169ad16f24ba39fa3aa31d47963b7
# 54f155d61b6f420ba309a052ac356296
#
#http://shop.mengguochengzhen.cn/mgcz/mobi/rpcmg/login?client_system=11.3&client_version=2.4.0&equipment_type=1&mac_address=02:00:00:00:00:00
#sid=2f273694-97cb-4616-aa30-df4816cc42d9
#

dd =session.post('http://shop.mengguochengzhen.cn/mgcz/mobi/shoppingCar/delete?',
                             data={'mId':'25da4ed0e6344b448eacb337d961a43a','scIds':'e28d9ac6bd4b4fa596174f88f4ef2247'},headers={'Cookie':'sid=01cf82b9-1a96-4020-8949-047b05ff7357'})
print(dd.text)