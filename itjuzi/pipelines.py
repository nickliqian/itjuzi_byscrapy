# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime
import json
from settings import MONGODB_HOST,MONGODB_PORT,MONGODB_DB,MONGODB_DB_SHEET


class ItjuziPipeline(object):
    def __init__(self):
        self.filename = open('okjuzi.json','w')

    def process_item(self, item, spider):
        item['catchTime'] = str(datetime.utcnow())
        item['spidername'] = spider.name

        data = json.dumps(dict(item),ensure_ascii=False) + '\n'

        self.filename.write(data.encode('utf-8'))

        return item

    def spider_close(self,spider):
        self.filename.close()


# class MongoDBItjuziPipeline(object):
#     def __init__(self):
#         client = pymongo.MongoClient(host=MONGODB_HOST,port=MONGODB_PORT)
#         db = client[MONGODB_DB]
#         self.sheet = db[MONGODB_DB_SHEET]
#
#
#     def process_item(self,item,spider):
#
#         data = dict(item)
#         self.sheet.insert(data)
#
#         return item


