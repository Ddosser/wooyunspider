# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
import pymongo
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline,DropItem
from datetime import datetime


class WooyunPipeline(object):
    def __init__(self):
        self.__db_host = "127.0.0.1"                      #数据库主机地址
        self.__db_port = 27017                            #数据库连接端口（默认为27017)
        self.__database = "wooyun"                        #数据库
        self.__client = pymongo.MongoClient(self.__db_host, self.__db_port)#建立数据库连接
        self.__db = self.__client[self.__database]                        #选择数据库
        self.__db.authenticate("wooyun","5fsQgrQSYXg4")
        self.__db_posts = self.__db.posts

        self.__total_records = 0
        self.__newtotal_records = 0
        #self.__log = None
    def open_spider(self, spider):
        self.__log = open("logs.log","r+")
        self.__total_records = self.__log.readline(-2).split("|")[0]

        
    def close_spider(self, spider):
        #self.__log = open("logs.log","w")
        data = str(self.__total_records) + "|     " + str(datetime.utcnow()) + "\n"
        self.__log.write(data)
        self.__log.close()
        self.__client.close()                                            #当spider关闭则关闭数据库连接

    def process_item(self, item, spider):
        css = "/css/style.css?v=201501291909"                            #叠层样式地址，需要更换成本地相对地址，这是需要在原html源码里匹配的字符串。
        re_css = "../../static/css/style.css"                                        #新css路径
        js = "https://static.wooyun.org/static/js/jquery-1.4.2.min.js"   #需要替换的js位置
        re_js = "../../static/js/jquery-1.4.2.min.js"

        if item['images']:                                               #如果有图片，则把图片的地址换成本地地址,images存放有图片的path,url和checksum值
            for it in item['images']:
                p = re.compile(it['url'])
                if p.search(item['html']):
                    item['html'] = item['html'].replace(it['url'],"../../static/images/" + it['path'])
        
        item['html'] = item['html'].replace(css,re_css).replace(js, re_js)#替换css和js

        self.__newtotal_records = item['total_records']
        if self.__total_records == self.__newtotal_records:
            self.close_spider(spider)

        post = {                                                          #数据表结构，dictionary型
            "Title": item['title'],
            "Vul_Type": item['vul_type'],
            "Author": item['author'],
            'Date': item['date'],
            'Open Time': item['open_time'],
            'Images': item['images'],
            'Content': item['html']
        }
        self.__db_posts.insert(post)                     #执行插入，将数据插入到数据库

        return item

class WooyunImagesPipeline(ImagesPipeline):             #这个ImagePipeline用来下载图片，但下载下来的图片用hash值作为文件名，不是原来的文件名
    def __init__(self,args):
        pass

    def file_path(self, request, info):             #想用这个方法来更改文件名，但未成功，还在查。
        image_guid = request.url.split('/')[-1]
        path = 'full/%s' % (image_guid)
        return path

    def get_media_requests(self, item, info):       #生成图片Request的url
        for image_url in item['image_urls']:
            yield Request(image_url)

    def item_completed(self, results, item, info):  #图片下载完成后执行的方法
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths

        return item
