#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
cnbeta
http://www.cnbeta.com/articles/200000.htm
'''
from dirbot.items import TextItem
from dirbot.items import Text2Item

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy import log
from scrapy import Spider
import scrapy
import json
import sys
import hashlib   
from dborm.settings import push_url
from dborm.settings import isexist_url
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc

log.msg("This is a warning", level=log.WARNING)

reload(sys)
sys.setdefaultencoding("utf-8")

def Catch0(list):
    if len(list) > 0:
        return list[0]
    else:
        return "null"

def mm5(l):

    m2 = hashlib.md5()   
    m2.update(l)   
    return m2.hexdigest()   

class MininovaSpider(Spider):

    name = 'cnbeta'
    allowed_domains = ['www.cnbeta.com']

    cnt_now = 473912
    cnt_min = 200000
    # cnt_max = 1500
    NUM_THREAD = 20
    url_temp = "http://www.cnbeta.com/articles/%d.htm"


    def start_requests(self):
        ret = []
        for i in xrange(self.NUM_THREAD):
            ret.append(self.make_requests_from_url( self.url_temp % (self.cnt_now - i)))
        self.cnt_now = self.cnt_now - self.NUM_THREAD
        return ret

    def parse(self, response):

        # bfortue = response.xpath('//a[@class="bn_a on"]/text()').extract()
        # bfortue_c = Catch0(bfortue)
        

        a = '//section[@class="article_content"]'

        data = response.xpath(a)
        infos = data.xpath('string(.)').extract()

        content = Catch0(infos)

        if content  == "null" or len(content) < 20:
            log.msg("NO non no conent\n", level=log.WARNING)

        else:
            item = TextItem()
            lent = len(content)
            item['text'] = content
            log.msg(content)
            yield item

            # if bfortue_c == "财经":
                # item2 = Text2Item()
                # item2['text'] = content
                # log.msg("财经")
                # yield item2
        
        self.cnt_now = self.cnt_now - 1
        if self.cnt_now > self.cnt_min:
            newurl = "http://www.cnbeta.com/articles/%d.htm" % self.cnt_now
            log.msg(">>URL=" + newurl )
            yield scrapy.Request(newurl, meta = {
                      'dont_redirect': True,
                      'handle_httpstatus_list': [302]
                  }, dont_filter=True)

