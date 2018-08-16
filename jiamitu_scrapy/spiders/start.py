# coding:utf-8
from scrapy import cmdline

# use  CLOSESPIDER_ITEMCOUNT to limit count
cmdline.execute("scrapy crawl jiamitu_spider".split())