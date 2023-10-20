import requests

#res = requests.get(url='http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getRegionProvince')
#print(res.text)
#打印响应主体内容，字符串格式
#requests.post("auth HTTP/1.1")
res=requests.post("https://akpufey.iot.gz.baidubce.com/auth",
headers={"Accept":"application/json","Content-Type": "application/json"},
json={"username":"thingidp@akpufey|kongzhi001|0|MD5","password":"fb6b96cfb6b85d1d355cc75fe7da51ba","tokenLifeSpanInSeconds":3000}
)
print(res.status_code)
print(type(res.text))
#print(res.text)
mydict=res.text
#print(type(mydict))
#print(mydict)

import json


r = json.loads(res.text) # json数据自动按Unicode存储
m=r["token"]
res2=requests.post("https://akpufey.iot.gz.baidubce.com/pub?topic=AAA&qos=0",
headers={"Accept":"application/json","Content-Type": "application/octet-stream","token":m},
data="Abc123mynameisyangfengh12322123131111111112133233ua"
)


print(res2.status_code)
print(res2.text)