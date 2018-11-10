# _*_ coding:utf-8 _*_
__author__ = 'boby'
__date__ = '2018/5/19 0019 下午 3:41'

from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware
import urllib.request

IPPOOLS= urllib.request.urlopen('http://tpv.daxiangdaili.com/ip/?tid=559126871522487&num=1&foreign=only').read().decode('utf8',"igonre")
class Ippl(HttpProxyMiddleware):
    def __init__(self,ip=''):
        self.ip=ip
    def process_request(self,request,spider):
        print("当前使用的代理IP是："+str(IPPOOLS))
        request.meta['proxy']= "http://"+str(IPPOOLS)
