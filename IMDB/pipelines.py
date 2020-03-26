# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
import logging
logger = logging.getLogger(__name__)
import re


class ImdbPipeline(object):
    def open_spider(self, spider):
        # 实例化client
        client = MongoClient()
        self.collections = client['IMDB']['movie']

    def process_content(self, item):
        # 过滤数据
        item['title'] = re.sub(r"\xa0|\s|\r|\n|\t", "", item['title'])
        item['year'] = re.sub(r"\n", "", item['year'])
        box = [re.sub(r"\xa0|\s|\r|\n|\t", "", i) for i in item['box'] if len(i)>0]
        item['box'] = [i for i in box if len(i)>0]
        item['cate'] = [re.sub(r"\xa0|\s|\r|\n|\t|\\", "", i) for i in item['cate']]
        item['cate'] = [i for i in item['cate'] if len(i)>0]
        logger.warning(item)
        return item

    def process_item(self, item, spider):
        # 存储数据
        item = self.process_content(item)
        self.collections.insert(dict(item))
        return item


