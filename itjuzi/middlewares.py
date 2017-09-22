#coding=utf-8
from settings import USER_AGENTS
import random
import base

ProxyIP = [
        '58.240.53.196:80',
        '61.136.163.245:8103',
        '202.99.99.123:80',
        '222.136.26.57:8888',
        '188.166.221.165:8080',
        '183.30.197.86:9797',
        '110.171.228.21:3128',
        '85.159.2.171:8080',
        '103.206.161.234:63909',
        '185.17.132.113:53281',
        '45.76.100.147:8080',
        '197.210.252.39:8080',
        '36.236.109.245:3128',
        '171.255.199.131:80',
        '115.52.252.9:8118',
        '36.74.103.228:8080',
        '177.230.105.9:65309',
        '103.252.186.212:8080',
        ]

class MyCustomDownloaderMiddleware(object):
    def process_request(self,request,spider):
        user_agent = random.choice(USER_AGENTS)
        print '本次使用的User-Agent:',user_agent
        request.headers.setdefault('User-Agent',user_agent)

class RandomProxyIP(object):
    def process_request(self,request,spider):
        proxy = random.choice(ProxyIP)
        request.meta['proxy'] = "http://" + proxy
        print '选择的IP：',request.meta['proxy']
