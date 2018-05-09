#
import json


d = {'no': 1, 'name': "un", 'url': ['www.baidu', 'sadfasdf', 'sdafsdfa'], 'aa': {'a': 1, 'b': 2}}

js = json.dumps(d)      # 转换成字符串格式

print(d)
print(repr(d))
print(js)

d2 = json.loads(js)     # 转换成json格式
print(d2)

with open('data.json', 'w') as f:
    json.dump(d, f)


with open('data.json', 'r') as f:
    data = json.load(f)

print(data)

print(d['url'])
print(data.get('url'))