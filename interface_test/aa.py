# 接口测试
import requests
import json

# post请求
def postRequest(url, json=None, data=None, headers=None):
    return requests.post(url, json=json, data=data, headers=headers)    # json格式参数，headers信息，data(可传入文件)等用法

url = 'http://scmapi.fanqiebianli.com/api/v1/shopinventory/getShopHomeInfoByCondition'       # url:接口地址
data_json = {'city': "", 'current': 1, 'pageNum': 1, "pageSize": 20, "qrCode": "", 'shop': ""}    # data:接口传递的参数
headers = {"Access-Token": "H5-ee560a5e32b64f4887e33eff92751bea"}                            # header:传递header信息
r = postRequest(url, json=data_json, data=None, headers=headers)
print('='*10, r.url)
# print("==utf8:  ", r.text.encode('utf8'))       # 获得的返回数据使用text方法进行获取
print("==普通:  ", r.text)
print(r.status_code)
rj = json.loads(r.text)     # 将返回文本转换为json格式
print(rj)
print(rj["code"], rj["message"], rj["data"]["list"][0]["shopNo"])       # 读取json中的数据


url = 'http://scmapi.fanqiebianli.com/api/v1/waveRest/getWaveChildByOrdernumberRest'       # url:接口地址
data_json = {"orderNumber": "QO20180425000423"}    # data:接口传递的参数
headers = {"Access-Token": "H5-ee560a5e32b64f4887e33eff92751bea"}                            # header:传递header信息
r = postRequest(url, json=data_json, data=None, headers=headers)
print('='*10, r.url)
# print("==utf8:  ", r.text.encode('utf8'))       # 获得的返回数据使用text方法进行获取
print("==普通:  ", r.text)
print(r.status_code)

# get请求
def getRequest(url, params=None, headers=None):
    return requests.get(url, params=params, headers=headers)

url = 'http://www.baidu.com'                                        # 两种方式效果相同
content = {"action": "getweather", "_": "1525748589219"}
r2 = getRequest(url, params=content)
print('='*10, r2.url)
print("==utf8:  ", r2.text.encode('utf-8'))       # 获得的返回数据使用text方法进行获取
# print("==普通:  ", r2.text)
print(r2.status_code)
url = 'http://www.baidu.com?action=getweather&_=1525748589219'      #
r2 = getRequest(url)
print('='*10, r2.url)
print("==utf8:  ", r2.text.encode('utf-8'))       # 获得的返回数据使用text方法进行获取
# print("==普通:  ", r2.text)
print(r2.status_code)

url = 'http://scmapi.fanqiebianli.com/api/v1/getMenu'
content = {}
headers = {"Access-Token": "H5-cbe55b328f9f4ea9b70f77d056804147"}
r = getRequest(url, params=content, headers=headers)
print('='*10, r.url)                        # 获取请求内容
# print("==utf8:  ", r.text.encode('utf8'))   # 获得的返回数据使用text方法进行获取
print("==普通:  ", r.text)
print(r.status_code)                        # 获取状态码


url = 'http://scmapi.fanqiebianli.com/api/v1/replenishRest/getShopAreaByShopInventoryRest'
content = {}
headers = {"Access-Token": "H5-cbe55b328f9f4ea9b70f77d056804147", "Cache-Control": "no-cache", 'responseType': 'json'}
r = getRequest(url, params=content, headers=headers)
print('='*10, r.url)                        # 获取请求内容
# print("==utf8:  ", r.text.encode('utf8'))   # 获得的返回数据使用text方法进行获取
print("==普通:  ", r.text)
print(r.status_code)                        # 获取


#
print("="*200)
r = requests.delete(url, headers=headers)
print(r.text)
r2 = requests.put(url, data=None,  headers=headers)
print(r.text)
r3 = requests.options(url, headers=headers)
print(r.text)
r4 = requests.head(url, headers=headers)
print(r.text)
r5 = requests.patch(url, data=None, headers=headers)
print(r.text)

