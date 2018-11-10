# _*_ coding:utf-8 _*_
__author__ = 'boby'
__date__ = '2018/5/19 0019 下午 2:54'
from ganji.settings import UAPOOLS
import random
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

class Uagt(UserAgentMiddleware):
    def __init__(self,ua=''):
        self.user_agent=ua
    def process_request(self,request,spider):
        thisua= random.choice(UAPOOLS)
        self.user_agent=thisua
        request.headers.setdefault('User-Agent',thisua)
