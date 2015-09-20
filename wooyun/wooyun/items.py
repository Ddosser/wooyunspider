# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
#from scrapy import Item

class WooyunItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()      #存储文章标题
    vul_type = scrapy.Field()   #vulnerable type
    date = scrapy.Field()       #漏洞申报时间，其实应该还有公开时间
    open_time = scrapy.Field()  #公开时间,作为定期更新的依据,更新的数量用总记录来比较。
    html = scrapy.Field()       #文章html源码
    author = scrapy.Field()     #
    total_records = scrapy.Field() #
    image_urls = scrapy.Field() #文章里的图片地址
    images = scrapy.Field()     #已下载的图片
    #image_paths = scrapy.Field()#图片路径（本地路径）

    link = scrapy.Field()       #文章链接，用于爬取网站内容
    #next_page = scrapy.Field()  #指向下一页