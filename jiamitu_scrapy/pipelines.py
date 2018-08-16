# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.conf import settings
from scrapy.exceptions import DropItem

class JiamituScrapyPipeline(object):

    def __init__(self):
        self.item_limit_num = settings["CLOSESPIDER_ITEMCOUNT"]

    def open_spider(self, spider):
        self.current_item_num = 0
        self.file = open('result.jl', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        if self.item_limit_num == 0 or self.current_item_num < self.item_limit_num:
            line = json.dumps(dict(item),ensure_ascii=False) + "\n"
            self.file.write(line)
            self.current_item_num += 1
            return item
        else:
            raise DropItem('item exceed limit')
