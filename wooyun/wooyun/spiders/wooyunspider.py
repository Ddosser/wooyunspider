#!/usr/bin/env python
#coding:utf-8

import scrapy

from scrapy.spiders import Spider
from scrapy.selector import Selector
from wooyun.items import WooyunItem


author = "Ddosser"
version = "1.0"

class WooyunSpider(Spider):
    name = "wooyunspider"
    allowed_domains = ["wooyun.org"]
    start_urls = ["http://www.wooyun.org/bugs/new_public/"]

    def __init__(self):
        self.__total_records = 0

    def parse(self, response):
        sel = Selector(response)
        total_pages = sel.xpath("//p[@class='page']/text()").re('\d+')[1]
        self.__total_records = sel.xpath("//p[@class='page']/text()").re('\d+')[0]
        links = sel.xpath('//tbody/tr/td/a/@href').extract()

        for url in links:                  #获取每一页的文章url，并发出请求，以获得html源码
        #for l in link[0:2]:
            url = response.urljoin(url)
            yield scrapy.Request(url, self.get_content)

        #for n in range(2,int(total_pages) + 1):         #构造下页地址，并循环回调。
        for np in range(2,2):                             #Test
            page = r"/bugs/new_public/page/" + str(np)
            url = response.urljoin(npage)
            yield scrapy.Request(url, self.parse)


    def get_content(self,response):             #获得网站内容
        sel = Selector(response)
        item = WooyunItem()
        item['title'] = sel.xpath('//title/text()').extract()[0].split("|")[0]
        item['vul_type'] = sel.xpath("//h3[@class='wybug_type']/text()").extract()[0].replace('\t', '').replace('\n', '').split(u'：')[1]
        item['date'] = sel.xpath("//h3[@class='wybug_date']/text()").re("[\d+]{4}-[\d+]{2}-[\d+]{2}")[0]
        item['open_time'] = sel.xpath("//h3[@class='wybug_open_date']/text()").re("[\d+]{4}-[\d+]{2}-[\d+]{2} [\d+]{2}:[\d+]{2}")[0]
        item['author'] = sel.xpath("//h3[@class='wybug_author']/a/text()").extract()[0]
        item['html'] = sel.xpath('/*').extract()[0]
        item['image_urls'] = sel.xpath("//img[contains(@src, 'http://static.wooyun.org/wooyun/upload/')]/@src").extract()
        item['total_records'] = self.__total_records
        return item
