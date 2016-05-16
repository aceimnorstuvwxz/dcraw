'''
(C) 2016 Unicall

Description: Spider for Lagou.com

Author: chenbingfeng
'''
from dirbot.items import CompanyItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy import log
from scrapy import Spider
import scrapy
import json
import sys
from dborm.settings import push_CompanyItem

reload(sys)
sys.setdefaultencoding("utf-8")

def Catch0(list):
    if len(list) > 0:
        return list[0]
    else:
        return "null"

class MininovaSpider(Spider):

    name = 'lagou'
    allowed_domains = ['lagou.com']
    page_index = 0
    page_index_max = 10000
    start_urls = ['http://www.lagou.com/gongsi/0.html']



    def parse(self, response):
        item = CompanyItem()
        log.msg("======>log test", level=log.INFO)
        
        if Catch0(response.xpath('//*[@id="container"]/div/text()').extract()) == "null" :
        
            item['name'] = Catch0(response.xpath('/html/body/div[3]/div/div/div[1]/h1/a/text()').extract()).encode('utf-8').strip()
            item['description'] = Catch0(response.xpath('//*[@id="company_intro"]/div[2]/div[1]/span[1]').extract()).encode('utf-8')[30:-7].strip()
            if item['name'] != "null":
                yield item
        
        if self.page_index < self.page_index_max:
            yield scrapy.Request('http://www.lagou.com/gongsi/%s.html' % self.page_index, self.parse)
            self.page_index = self.page_index + 1
        
''' local test
        f = open("t.out","a")
        f.write(item['name'])
        f.write(item['description'])
        f.close()
'''
