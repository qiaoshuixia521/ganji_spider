# _*_ coding:utf-8 _*_
__author__ = 'boby'
__date__ = '2018/5/17 0017 下午 8:56'

from scrapy.cmdline import execute
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(['scrapy','crawl','ganji'])
execute(['scrapy','crawl','loginspd1'])