#!/usr/bin/env python
#coding:utf-8

import os
import scrapy
import math
from scrapy.spiders import Spider
from scrapy.selector import Selector
from wooyun.items import WooyunItem
from wooyun.settings import *


author = "Ddosser"
version = "1.2"

class WooyunSpider(Spider):
    name = "wooyunspider"
    allowed_domains = ["wooyun.org"]
    start_urls = ["http://www.wooyun.org/bugs/new_public/"]

    def __init__(self):
        self.__total_records = 0
        self.__update_records = 0
        self.__IS_ENDPAGE = False
        #检查数据库进程是否开启，如果未开启，则打开，不然爬虫无法连接
        reply = os.popen("ps -ef |grep 'mongod' |awk '{print $8}'").readlines()[0].replace("\n","").strip()
        if reply is not "mongod":
            os.system(MONGODB_CMD)
        else:
            print "\033[1;32m [*] Mongodb is already runing \033[0m"

    def parse(self, response):
        sel = Selector(response)
        total_pages = int(sel.xpath("//p[@class='page']/text()").re('\d+')[1])
        self.__total_records = int(sel.xpath("//p[@class='page']/text()").re('\d+')[0])

        if IS_FIRSTTIME_CRAWL:                           #第一次爬取
            for np in xrange(1, total_pages + 1):         #构造下页地址
                npage = r"/bugs/new_public/page/" + str(np)
                url = response.urljoin(npage)
                yield scrapy.Request(url, self.get_urls) 
        else:                                                #更新爬取
            update_records = self.__total_records - int(OLD_TOTAL_RECORDS)

            if update_records > RECORDS_PER_PAGE:
                update_pages = int(update_records/RECORDS_PER_PAGE)
                if (update_records%RECORDS_PER_PAGE) > 0:
                    update_pages = update_pages + 1
            elif update_records >=0 and update_records <= RECORDS_PER_PAGE:
                update_pages = 0

            #print "\033[1;31m" + str(update_records) + "\033[0m"

            for np in xrange(1, update_pages+1):         #构造下页地址
                npage = r"/bugs/new_public/page/" + str(np)
                url = response.urljoin(npage)
                if np == update_pages and (update_records%RECORDS_PER_PAGE) > 0:
                    self.__update_records = update_records
                    self.__IS_ENDPAGE = True
                yield scrapy.Request(url, self.get_urls)         

    def get_urls(self, response):
        sel = Selector(response)
        links = sel.xpath('//tbody/tr/td/a/@href').extract()
        if self.__IS_ENDPAGE:
            links = links[0:self.__update_records%RECORDS_PER_PAGE + 1]
        for url in links:                  #获取每一页的文章url，并发出请求，以获得html源码
        #for l in link[0:2]:               #For Test
            url = response.urljoin(url)
            yield scrapy.Request(url, self.get_content)    

    def get_content(self,response):             #网站内容
        sel = Selector(response)
        item = WooyunItem()
        item['title'] = sel.xpath('//title/text()').extract()[0].split("|")[0]
        item['vul_type'] = sel.xpath("//h3[@class='wybug_type']/text()").extract()[0].replace('\t', '').replace('\n', '').split(u'：')[1]
        item['wooyunid'] = sel.xpath("//h3[1]/a[contains(@href, '/bugs/wooyun-')]/text()").extract()[0]
        item['date'] = sel.xpath("//h3[@class='wybug_date']/text()").re("[\d+]{4}-[\d+]{2}-[\d+]{2}")[0]
        item['open_time'] = sel.xpath("//h3[@class='wybug_open_date']/text()").re("[\d+]{4}-[\d+]{2}-[\d+]{2} [\d+]{2}:[\d+]{2}")[0]
        item['author'] = sel.xpath("//h3[@class='wybug_author']/a/text()").extract()[0].encode('utf-8')
        #item['html'] = sel.xpath('/*').extract()[0].encode('utf-8')
        item['html'] = ""
        item['total_records'] = self.__total_records
        if SAVE_IMAGES:
            item['image_urls'] = sel.xpath("//img[contains(@src, 'http://static.wooyun.org/wooyun/upload/')]/@src").extract()
        else:
            item['image_urls'] = []
        return item
