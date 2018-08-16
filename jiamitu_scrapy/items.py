# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BabyInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    generation = scrapy.Field()
    rareDegree = scrapy.Field()
    price = scrapy.Field()

class ParentInfoItem(scrapy.Item):

    id = scrapy.Field()
    generation = scrapy.Field()
    rareDegree = scrapy.Field()
    FIGURE = scrapy.Field()
    BODY_COLOR = scrapy.Field()
    MOUTH = scrapy.Field()
    EYE = scrapy.Field()
    EYE_COLOR = scrapy.Field()
    PATTERN = scrapy.Field()
    PATTERN_COLOR = scrapy.Field()
    PROPERTY = scrapy.Field()
