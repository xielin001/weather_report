#-*- coding:utf-8 -*-
import pprint
def city(file):
    with open(file,'r',encoding='UTF-8') as f:
        temp = []
        for line in  f.readlines():
            if line != '\n':
                temp.append(line.strip('\n'))
        citys = {}
        for string in temp:
            k,j = string.split('=')
            citys[j] = k
    return citys
if __name__=="__main__":
    citys = city('citycode2.txt')
    for city in citys:
        pprint.pprint(city + ":" +citys[city])