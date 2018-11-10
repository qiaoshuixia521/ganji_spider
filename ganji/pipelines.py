# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
class GanjiPipeline(object):
    def open_spider(self,spider):#爬虫启动时，链接数据库
        self.con=sqlite3.connect('zufang sqlite')
        self.cn=self.con.cursor()


    def process_item(self, item, spider):#执行数据库的插入操作
        insert_sql='insert into zufang(title,money) values("{}","{}")'.format(item['title'],item['money'])
        print(insert_sql)
        self.cn.execute(insert_sql)
        self.con.commit()#必须进行数据的提交
        return item

    def spider_close(self,spider):#关闭数据库
        self.con.close()
