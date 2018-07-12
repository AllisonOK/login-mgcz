# -*- coding: UTF-8 -*-
import re
import time
import random
import requests
from selenium import webdriver
import pymysql
import openpyxl

wb = openpyxl.load_workbook('1.xlsx')
sheet = wb.get_sheet_by_name('脚本')
arr = []
for row in sheet.rows:
    for cell in row:
        if cell.value==None:
            break
        else:
            arr.append(cell.value)
su =int(len(arr)/12)


url = 'http://mall.mengguochengzhen.cn'


driver = webdriver.Chrome()
driver.get(url+'/mgcz/system/index')
driver.find_element_by_id('form-username').send_keys('13971229922')
driver.find_element_by_id('form-password').send_keys('qq74108520')
driver.find_element_by_xpath('//*[@id="login-form"]/button').click()
time.sleep(5) #拿登陆后的最新cookies
# 获取cookie信息
cookies = driver.get_cookies()

sid=cookies[1]['value']
JSESSIONID=cookies[0]['value']

session = requests.session()  # 商家用户


def set_up():
    requests_login111 = session.get(url + '/mgcz/admin/commodity',headers={'Cookie': 'JSESSIONID=' + JSESSIONID + '; sid=' + sid})
    Cid = re.findall('<button title="编辑" class="btn btn-xs btn-primary edit" data-keyId="(.*?)"',requests_login111.text)

    return Cid[0]

def cnId(size_name,size_value):
    on1= {'尺寸奶锅16cm/汤锅20cm/蒸锅24cm':'06dc7ffecafa4b759602d6b8099b8068',
          '尺寸奶锅16cm/汤锅20cm/煎锅24cm':'0842ae0ac8b646b29c45d317c8d9a43c',
          '尺寸2.0L':'0e61137db2624f8e8ea545e65be4dd0e',
          '尺寸16cm/20cm/24cm/24cm':'24dff2b749424f679774d749e376106f',
          '尺寸32/24/24CM':'2538be0bed5048d991e45a0c41c3772a',
          '尺寸汤锅20cm/煎锅24cm':'25b87528b24d40e6b8bf05ffa328b13e',
          '尺寸16cm':'27942803663a42adb9f4c4ac865fa174',
          '尺寸 24/24/18 CM':'289c562ba0ef4267827f4367129f8521',
          '容量1000ml/3000ml':'28e700bc397146e09b7e1ad9b8a40183',
          '尺寸2500ml ':'40a7fbbb391e4ce5b9d36222aa468a87',
          '尺寸锅铲36cm/汤勺34cm/漏勺37cm':'41e9976a297e45249d4e496f4dcd0144',
          '尺寸26cm':'4bdc86422b0047ccb000caefc6da530b',
          '尺寸奶锅16cm/汤锅20cm/煎锅24cm':'50d823842e4d4c409637a8f3b8ef2f44',
          '尺寸火锅28cm/炒锅30cm':'570421e4983c4eb5804324b6228623a3',
          '尺寸32CM/24CM/24CM':'5773ee7f88834b788fffe038e6023441',
          '尺寸30cm':'6036c585c19a46a583d5f088de3ea97b',
          '数量6件套':'67e8a71662d440c3bd8e56a3991926c4',
          '尺寸28cm':'6992390282b24a689526f00b4888e671',
          '尺寸23*40CM':'7034b989b2be49ceb53a7a1973eaa91f',
          '尺寸奶锅18cm/汤锅22cm':'7467e7b90447429e8802799af0394730',
          '尺寸28x28x6.6CM':'886805cebd994d6284a8802c6852ec05',
          '尺寸425x110x360mm':'961724cbe2d64ee58c755e8d6035dc3f',
          '尺寸1.9L':'9ed404d5d0594bc3befb550fed0f4790',
          '尺寸32*32*8 CM（锅体）':'a2e301433a564375adb269842fa2df59',
          '尺寸24cm':'a4041dd4a570428abfb14ea4e528470d',
          '尺寸16cm/20cm/24cm/24CM':'af464836d5d8405ba3b49e0f5010a489',
          '尺寸34.5cm/32.5cm/21cm':'b3243d378d604ef2935d7d71704b7e02',
          '容量0.5L-1L-3L':'b57c09b641354213befe79868b407889',
          '尺寸32cm':'bac73641fa4343369236f8854c0119d8',
          '尺寸24CM+32CM':'c103461c72614d5ca4f0e7ebdc0829cd',
          '尺寸32CM   (62x34x24cm)':'c1b2cb8d7c1a41af801251f2b95e308a',
          '尺寸48*28CM':'c3f0e26196aa47f98561207976c9198c',
          '尺寸37cm*18cm*22cm':'c69a7d0f384a4eefa66a37151c04fb45',
          '尺寸20cm ':'d422885362f2407cbc0a98dedf552a9c',
          '尺寸18cm':'d5c3f60c8bf640fba2a0f8100d57ede6',
          '尺寸22cm':'db12cbb057364d0abc6f263684b8e9a7',
          '尺寸24cm  26cm  28cm':'de6cc71aed97460abaff9b27a9898aef',
          '尺寸4000ML':'e6d8d20ab96e4004a746a9320affc0fe',
          '尺寸火锅28cm/炒锅30cm':'ea87de74208044759ddde8928f0bf3e7',
          '容量3000ml':'f225a8b74a634743a7bdeb36c6a482d2',
          '尺寸30CM/22CM':'fad2d59ffd8f489f9815f682693b27f6'
          }
    try:
        kk=on1[size_name+size_value]
    except:
        return 0
    else:
        return kk



def one_class(one):
    one_class = {'家装建材':'05075f5627d54fe0b02a27b7df817765',
                 '汽车用品':'05a1c11d9f5e4915ade964786a0f036b',
                 '便民服务':'0620ec0ec03440dcb3fc2b1b5d203fab',
                 '百货市场':'0e905b818a124d03986bc79883b44ecf',
                 '美酒佳酿':'0fbd5ca897824db096b2a1542b0b09d0',
                 '居家家纺':'61aca34b893d454b9b3943410f18562f',
                 '母婴用品':'6c814cea136449859f2793d3659e0a23',
                 '家电办公':'7c208465238b40dfbaaf1e96105c3dfd',
                 '鞋类箱包':'7e0a8dbf4ceb4bae8c8fd1a0081eb352',
                 '护肤彩妆':'80e4884ebd9342a18979215321e822e8',
                 '珠宝配饰':'ad86951f8c75452ea047c44af2dd0b6a',
                 '汇吃美食':'b7cda19895dd4e76844a024568f5239a',
                 '衣着服饰':'c8b1e1d4a7b145ce88679cf42e02c8e0',
                 '影音数码':'e5ec0199df8a4d0f806f3224a2ef9f11',
                 '休闲旅游':'e9e978639fa34400bc360fab34710aa9'}
    try:
        kk=one_class[one]
    except:
        return 0
    else:
        return kk
def two_class(two):
    two_class = {'私人飞机':'07be8564752e401382f2306b9f39b449',
                 '葡萄酒':'08923b6d71f948bb89bd0952b797c1d2',
                 '儿童服饰':'0e3b64b5d7bc482a82795615d0d23832',
                 '美发造型':'155873dac46f46dfa5bf8e796d636cc9',
                 '个人清洁':'16a6ef4ad0024c0e9f8d2e51af2c533a',
                 '运动服饰':'225f28f8569044be8e9fe19f27ee2ded',
                 '生鲜果蔬':'2294677df9344895a90652a46c94665f',
                 '休闲零食':'24ccbffa68c643759148877595f50d2e',
                 '出境邮轮':'256e2de5888d426fb8570ad77c37f155',
                 '时尚彩妆':'259d4e3db2854e18b3568d1586969954',
                 '汽车租赁':'2b598ea36f8546d9b115b55a6e15b46b',
                 '畅游欧洲':'2c2d9e6ae81445eebc79feca44ed7e76',
                 '潮流女包':'3041a220c0024434821151205039d0e5',
                 '灯具灯饰':'324a8d1118c44b7b94cea58bcb4a2ed4',
                 '品质手表':'381e2ad52f294f7ab5fa7ba747e1665b',
                 '商务男鞋':'3ff629627bd744b1b1c377b4364931da',
                 '辅助营养':'426fa32071d94f74bb81ba8f62883426',
                 '滋补养生':'47d32023c6144663964359861f81c128',
                 '时尚女鞋':'518abe0a309846558aaf7b2ec265ae87',
                 '厨房工具':'52db4e73133d43f8af643feda5ad8e27',
                 '潮流童鞋':'53a66cbb6500482aaf091e404881c0c3',
                 '养生滋补':'5d36922034e441cca084958c6da8b11c',
                 '进口洋酒':'5e607ec955474a3bb8eec1f33c7f69fb',
                 '文玩新宠':'5e92544be9df437d80e5ee2348859327',
                 '居家日用':'604100071a3f48a09c402f1d1b07e59e',
                 '爽口啤酒':'616e1b6ec1fb4f6fb0d60b45badc8e68',
                 '休闲男鞋':'616e98eb157943bd937ce1a52c46c6e1',
                 '翡翠玉石':'6261a670cbc44d378fb7500d25efc314',
                 '美容仪器':'62bd41b26f2b4a778f41489fc80f1982',
                 '身体护理':'6654267ea6694b3ba9ddaaa508b0bf67',
                 '居家服饰':'6b57239e4aac40a5afdaa3953ff2b540',
                 '中年女装':'6f67a351d643459cbbc2ee30a8217622',
                 '手机电脑':'6f6d2fc8d70242d5bf231a45ae4a9331',
                 '四季茗茶':'737e973a536c4340bdf58d8c38ac1c7a',
                 '五金工具':'8069b3f5458846dda9552eb149dba058',
                 '夏凉床品':'82e9726fa7674fd6be5d90a37961320b',
                 '服饰配件':'858556d30ce548fe89497e0d5a3b5b8d',
                 '家居摆件':'8755763b58db4026bfdf04eb9f7c7817',
                 '卫浴用品':'887885d9f9b04e4cb72f4fba28cfc02f',
                 '计生用品':'8b270581405744c7bcdce516e27f0b62',
                 '潮流眼镜':'8d06e046b92a44b19ed6d9be49e68d71',
                 '精品男包':'8f83fccc6fc24aed999c673f92e32799',
                 '厨房电器':'92b89c4f5603467398afa06b3c1d40bf',
                 '运动潮鞋':'95c162ced5eb41c48844182a112bab30',
                 '运动户外':'a0d3bb6f7b784a49a6e9b33172f91c30',
                 '儿童玩具':'a5285898d75741e6a6615ded0f97b3bd',
                 '全季床品':'a7179b6b20574768a525ee742bb7beb4',
                 '绅士用品':'a965ee3a217b46a9be8602576aa6f587',
                 '中年男装':'ab1b1a9ab93d4572a8376ae0a8348e0e',
                 '其他个护':'ac87a06b3b4143fbb6a284d84815804f',
                 '游艇租赁':'af127ece1df14a969fd2e0a01ef01561',
                 '商务女装':'b5699f19a8b34b9fa9748d28648b4e77',
                 '面部护理':'b7524b15e4784ab4bec563718e23672d',
                 '数码配件':'b9d0dd33d75245809e92e0bcdbd20de4',
                 '潮流女装':'bba96804708a4ff0a295c4dbead83bcd',
                 '牛奶饮料':'be0b4d474cbd4eac9a16341907bf926a',
                 '家用电器':'c081cfe07b4540e1a017b20257a5da27',
                 '会员充值':'c129020c7b4b4328baa580b5edc4927c',
                 '影音配件':'c206b77ea8e848e286e7a759421c2917',
                 '居家布艺':'c2cea60623d7469e995c26ede319af08',
                 '醇香白酒':'c7b32f9c92194b99928408fef60210fc',
                 '超值套装':'c9f28ec9bafc48a2ace45654bed24e94',
                 '精品家具':'cafb24f9aa6444018f0d9f941117222d',
                 '生活用品':'d190742412fc43c38630689838c9cf06',
                 '香氛精油':'d495f63d65b644dc9733a5be28ff194e',
                 '商务男装':'d6920a5dc86540f884c8faa68c0b47f9',
                 '时尚男装':'dc52b02b8bac43cbbd51f80d14f6591a',
                 '粮油调味':'dea16ae4e4cb4d4c81a1bd7c05c72a96',
                 '时尚饰品':'e7850d7ce40746d496e3e87f4a0ac74c',
                 '婴童用品':'eba9bb3cdea6429aabeacd53e4eb0ea9',
                 '内衣内裤':'f3c0300d50134efcb238a64390118544',
                 '生活电器':'f8967ee39b0a46a0ade1839667273729',
                 '美容清洗':'fc1db81ff3f14907b9c4ed1ca00e7a6e',
                 '时尚箱包':'fd1dadec1ad2432083ae0df2222506f0',
                 '个护电器':'fdde5930bd014b2b82c1dead967d7645',
                 '智能家居':'fde5809f62e84823969f0e6b2b80d600'}
    try:
        kk=two_class[two]
    except:
        return 0
    else:
        return kk
#上架商品
def up_shop(cname,gcode,stock,salesVolume,firstClassify,secondClassify,size_name,size_value):

    # 商家添加商品
    requests_save = session.post(url+'/mgcz/admin/commodity/save',
                                 data={ 'cname': cname, 'gcode': gcode, 'stock': stock,'salesVolume':salesVolume ,
                                        'firstClassify': firstClassify,
                                        'secondClassify': secondClassify, 'describes': '&nbsp;'},
                                 headers={'Cookie': 'JSESSIONID=' + JSESSIONID + '; sid=' + sid})

    request_set_specifications = session.post(url+'/mgcz/admin/commodity/bindingNorms',
                                              data={'cnId': cnId(size_name,size_value), 'cId': set_up()},
                                              headers={'Cookie': 'JSESSIONID=' + JSESSIONID + '; sid=' + sid})

def up_price(salePrice1,accountPrice1,stock1,specifications1):

    request_init_editPrice = session.post(url+'/mgcz/admin/commodity/init_editPrice',
                                          data={'cId': set_up(),
                                                'backParam': 'pageNO=1&pageSize=15&sort=a.create_date DESC&search_sort=a.create_date+DESC'} )
    salePrice= float(salePrice1)
    accountPrice = float(accountPrice1)
    requirePrice = salePrice - (salePrice - accountPrice) / 2
    gamePrice = int ((salePrice - accountPrice)/2)


    requests_saveCommodityPrice = session.post(url+'/mgcz/admin/commodity/saveCommodityPrice',
                                               data={ 'specifications': specifications1, 'commodityId': set_up(), 'salePrice': salePrice,
                                                      'gamePrice': gamePrice, 'requirePrice':requirePrice , 'accountPrice': accountPrice, 'stock': stock1},
                                               headers={'Cookie': 'JSESSIONID=' + JSESSIONID + '; sid=' + sid})
for ko in range(1,su):
    try:

        cname=arr[ko*12+1]
        gcode=arr[ko*12+2]
        stock=arr[ko*12+3]
        salesVolume=arr[ko*12+4]
        firstClassify=one_class(arr[ko*12+5])
        secondClassify=two_class(arr[ko*12+6])
        size_name=str(arr[ko*12+7])
        size_value=str(arr[ko*12+8])
        if set_up():
            up_shop(cname, gcode, stock, salesVolume, firstClassify, secondClassify, size_name, size_value)
        else:
            break


        specifications = str(size_value).split(',')
        salePrice = str(arr[ko*12+10]).split(',')
        accountPrice=str(arr[ko*12+11]).split(',')
        stock=str(arr[ko*12+9]).split(',')
        for k in range(0,len(specifications)):

            up_price(salePrice[k],accountPrice[k],stock[k],specifications[k])
    except:
        print(str(arr[ko*12])+'--------------------------------------------------------失败')
        continue
    else:
        print(str(arr[ko*12])+'-----------成功')
