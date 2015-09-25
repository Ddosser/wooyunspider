# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from wooyun.items import WooyunItem


class WooyunknowledgeSpider(Spider):
    name = "wooyunknowledge"
    allowed_domains = ["wooyun.org"]
    start_urls = [
        'http://drops.wooyun.org/'
    ]

    def parse(self, response):
        sel = Selector(response)
        # <span class="pages">第 1 页，共 80 页</span>
        total_page = sel.xpath("//div[@class='wp-pagenavi']/span[@class = 'pages']/text()").re(u"共 (\d+) 页")[0]
        #total_page = 1
        for page in xrange(1,int(total_page) + 1):
            page_url = "http://drops.wooyun.org/page/" + str(page)
            yield scrapy.Request(page_url, self.get_post_urls)

    def get_post_urls(self, response):
        sel = Selector(response)
        post_urls = sel.xpath("//div[@class = 'post']/h2[@class = 'entry-title']/a/@href").extract()
        for url in post_urls:
            url = response.urljoin(url)
            yield scrapy.Request(url, self.get_detail)

    def get_detail(self, response):
        sel = Selector(response)
        item = WooyunItem()
        item['post_title'] = sel.xpath("//title/text()").extract()[0].split(u"|")[0].strip()
        item['post_author'] = sel.xpath("//div[@class = 'entry-meta']/a/@href").extract()[0].split("/")[2]
        item['post_datetime'] = sel.xpath("//div[@class = 'entry-meta']/time/text()").extract()[0]
        item['image_urls'] = sel.xpath("//p/img/@src").extract()
        item['html'] = sel.xpath("/*").extract()[0]
        return item