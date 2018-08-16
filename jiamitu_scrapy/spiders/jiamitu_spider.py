# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import json
import math
from scrapy.conf import settings
from tools import TransCookie
from jiamitu_scrapy.items import BabyInfoItem, ParentInfoItem


class JiamituSpiderSpider(scrapy.Spider):
    name = "jiamitu_spider"
    allowed_domains = ["jiamitu.mi.com"]
    cookies = TransCookie(settings["COOKIES"]).string2dict()

    def start_requests(self):
        url = 'https://jiamitu.mi.com/pet/ng/listng'
        yield Request(url,callback=self.form_request,cookies=self.cookies)

    def form_request(self,response):
        try:
            total = json.loads(response.body)["result"]["total"]
            limit_num = 50
            for page_id in range(math.ceil(total/limit_num)):
                page_url = 'https://jiamitu.mi.com/pet/ng/listng?page=' + str(page_id) + '&limit=' + str(limit_num)
                yield Request(page_url, callback=self.parse_list, dont_filter=True)
        except Exception as e:
            self.logger.error("error occurred when form_request")

    def parse_list(self, response):
        try:
            baby_info_list = json.loads(response.body)["result"]["data"]
            for baby_info in baby_info_list:
                item = BabyInfoItem()
                item['id'] = baby_info['id']
                item['generation'] = baby_info['generation']
                item['rareDegree'] = baby_info['rareDegree']
                item['price'] = baby_info['price']
                yield item
                baby_detail_url = "https://jiamitu.mi.com/pet/ng/getng?gid=" + str(item['id'])
                yield Request(baby_detail_url, callback=self.parse_baby_detail)
        except Exception as e:
            self.logger.error("error occurred when parse_list")

    def parse_baby_detail(self, response):
        try:
            parents_info = json.loads(response.body)["result"]["parents"]
            for parent in parents_info:
                parent_detail_url = "https://jiamitu.mi.com/pet/detail?petId=" + str(parent['petId'])
                yield Request(parent_detail_url, callback=self.parse_parent_detail)
        except Exception as e:
            self.logger.error("error occurred when parse_baby_detail")

    def parse_parent_detail(self, response):
        try:
            parent_detail = json.loads(response.body)["result"]
            item = ParentInfoItem()
            item['id'] = parent_detail['id']
            item['generation'] = parent_detail['generation']
            item['rareDegree'] = parent_detail['rareDegree']
            item['FIGURE'] = parent_detail['FIGURE']
            item['BODY_COLOR'] = parent_detail['BODY_COLOR']
            item['MOUTH'] = parent_detail['MOUTH']
            item['EYE'] = parent_detail['EYE']
            item['EYE_COLOR'] = parent_detail['EYE_COLOR']
            item['PATTERN'] = parent_detail['PATTERN']
            item['PATTERN_COLOR'] = parent_detail['PATTERN_COLOR']
            item['PROPERTY'] = parent_detail['PROPERTY']
            yield item
            if "parents" in parent_detail.keys():
                parents_info = parent_detail["parents"]
                for parent in parents_info:
                    parent_detail_url = "https://jiamitu.mi.com/pet/detail?petId=" + str(parent['petId'])
                    yield Request(parent_detail_url, callback=self.parse_parent_detail)
        except Exception as e:
            self.logger.error("error occurred when parse_parent_detail")
