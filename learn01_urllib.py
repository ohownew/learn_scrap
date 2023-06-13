# 【2022 年】Python3 爬虫教程 - urllib 爬虫初体验 
# https://cuiqingcai.com/202221.html 

import urllib.request

response = urllib.request.urlopen('https://www.python.org')
# print(response.read().decode('utf-8')) # 抓取网页源代码

print(type(response)) # 抓取响应类型

print(response.status) # 状态码
print(response.getheaders()) # 响应头
print(response.getheader('Server')) # 服务器类型


# urlopen API
# urllib.request.urlopen(url, data=None, [timeout,]*, cafile=None, capath=None, cadefault=False, context=None)

## data 参数
import urllib.parse
# import urllib.request

data = bytes(urllib.parse.urlencode({'name': 'germey'}), encoding='utf-8')
response = urllib.request.urlopen('https://httpbin.org/post', data=data)
print(response.read().decode('utf-8'))