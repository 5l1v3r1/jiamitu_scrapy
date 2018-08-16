# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import log


class JiamituScrapyDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    def process_response(self,request,response,spider):
        if response.status != 200:
            log.logger.warning("response.status:" + str(response.status) + " url:"+request.url + " request again")
            return request
        return response