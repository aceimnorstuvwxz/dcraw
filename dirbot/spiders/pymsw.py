#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
濮院毛衫网
http://www.pymsw.cn/article-999-1.html
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

    name = 'pymsw'
    allowed_domains = ['www.pymsw.cn']

    cnt_now = 1400
    cnt_min = 0
    # cnt_max = 1500
    start_urls = ["http://www.pymsw.cn/article-0-1.html"]



    def parse(self, response):

        # bfortue = response.xpath('//a[@class="bn_a on"]/text()').extract()
        # bfortue_c = Catch0(bfortue)
        

        a = '//td[@id="article_content"]'

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
            newurl = "http://www.pymsw.cn/article-%d-1.html" % self.cnt_now
            log.msg(">>URL=" + newurl )
            yield scrapy.Request(newurl, meta = {
                      'dont_redirect': True,
                      'handle_httpstatus_list': [302]
                  }, dont_filter=True)

