#-*- coding:utf-8 -*-

#自定义一个输入异常
import json
import urllib
from urllib import request

from weather.file_read import city


class NoneInputError(Exception):
    def __init__(self,message):
        Exception.__init__(self)
        self.message = message
try:
    print("天气查询".center(20, '='))
    addr = input("请输入要查询的城市名称：")
    #print(addr)
    days = {'7天': 'weather', '今天': 'weather1d', '8-15天': 'weather15d'}
    for key in days:
        print(key + ':' + days[key])
    day = input("请输入要查询的时间：")
    if addr=='' or day =='':
        raise NoneInputError("未输入正确城市名称或时间")
except NoneInputError as e:
    print(e.message)
#定义一个字典存放查询时段

citys = city('citycode2.txt')
citycode = citys[addr]
#print(citycode)
url = "http://www.weather.com.cn/" + days[day] + '/' + citycode + ".shtml"
#print(url)
content = urllib.request.urlopen(url).read()
data = content.decode('utf-8')
#data = json.loads(content.decode('utf-8'))
print(data)