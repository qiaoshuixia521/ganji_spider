# _*_ coding:utf-8 _*_
__author__ = 'boby'
__date__ = '2018/5/18 0018 下午 7:26'

from bs4 import BeautifulSoup
import requests
import time

url="https://knewone.com/discover?page="


def get_page(url,data=None):
    wb_data=requests.get(url)
    soup=BeautifulSoup(wb_data.text,'lxml')
    print(soup)
    print(type(soup))
    imgs=soup.select('a.cover-inner>img')
    titles=soup.select('section.content>h4>a')
    links= soup.select('section.content>h4>a')

    if data==None:
        for img,title,link in zip(imgs,titles,links):
            data={
                'img':img.gt('src'),
                'title':title.get('title'),
                'link':link.get('href')
            }
            print(data)


def get_more_page(start,end):
    for one in range(start,end):
        get_page(url+str(one))
        time.sleep(2)


get_more_page(1,10)