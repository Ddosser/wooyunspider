# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
import pymongo
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline,DropItem
from settings import *
import time


class WooyunPipeline(object):
    def __init__(self):
        self.__database = DB_NAME                                            #数据库
        self.__client = pymongo.MongoClient(DB_SERVER, DB_PORT)              #建立数据库连接
        self.__db = self.__client[self.__database]                           #选择数据库
        self.__db.authenticate(DB_OWNER,DB_PASSWD)
        self.__dbcollection = self.__db[DB_COLLECTION]                       #选择记录集

        self.__total_records = 0

    def open_spider(self, spider):
        if IS_OPENBUG_SPIDER:
            self.__fp = open(LOGS_PATH, "a")
        
    
    def close_spider(self, spider):
        if IS_OPENBUG_SPIDER:
            wdata = str(self.__total_records) + "    |        " + \
            str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))) + \
            "\n"
            self.__fp.write(wdata)                                         #将记录写入记录日志里
            self.__fp.close()

        self.__client.close()                                            #当spider关闭则关闭数据库连接

    def process_item(self, item, spider):
        wooyun_openbug = {}
        wooyun_knowledge = {}

        if IS_OPENBUG_SPIDER:
            css = "/css/style.css?v=201501291909"                            #叠层样式地址，需要更换成本地相对地址，这是需要在原html源码里匹配的字符串。
            re_css = "../../static/css/style.css"                                        #新css路径
            js = "https://static.wooyun.org/static/js/jquery-1.4.2.min.js"   #需要替换的js位置
            re_js = "../../static/js/jquery-1.4.2.min.js"
            item['html'] = item['html'].replace(css,re_css).replace(js, re_js)#替换css和js

            if SAVE_IMAGES:          #如果有图片，则把图片的地址换成本地地址,images存放有图片的path,url和checksum值
                if item['images']:
                    for it in item['images']:
                        item['html'] = item['html'].replace(it['url'],"../../static/images/" + it['path'])
                    wooyun_openbug['Images'] = item['images']
                    # for img_url in item['image_urls']:
                    #     if 'http://' not in img_url:
                    #         url = response.urljoin(img_url)
                    #         item['html'] = item['html'].replace(img_url, url)
                    #         image_urls_list.append(url)

            if self.__dbcollection.find({'WooyunID':item['wooyunid']}) == []:
                wooyun_openbug = {                                                          #数据表结构，dictionary型
                    "Title": item['title'],
                    "WooyunID": item['wooyunid'],
                    "Vul_Type": item['vul_type'],
                    "Author": item['author'],
                    'Date': item['date'],
                    'Open Time': item['open_time'],
                    # 'Images': item['images'],
                    'Content': item['html']
                }
            self.__dbcollection.insert(wooyun_openbug)                #执行插入，将数据插入到数据库
            self.__total_records = self.__dbcollection.find().count()        
        else:
            jquery_js = "http://wooyun.b0.upaiyun.com/static/js/jquery.min.js"
            bootstrap_js = "http://wooyun.b0.upaiyun.com/static/js/bootstrap.min.js"
            main_css = "http://wooyun.b0.upaiyun.com/static/css/95e46879.main.css"
            bootstrap_css = "http://wooyun.b0.upaiyun.com/static/css/bootstrap.min.css"

            wooyun_jquery_js = "../../static/js/wooyun_jquery.js"
            wooyun_bootstrap_js = "../../static/js/wooyun_bootstrap.js"
            wooyun_main_css = "../../static/css/wooyun_main.css"
            wooyun_bootstrap_css = "../../static/css/wooyun_bootstrap.css"

            # image_urls = []
            item['html'] = item['html'].replace(jquery_js, wooyun_jquery_js).replace(bootstrap_js, wooyun_bootstrap_js)
            item['html'] = item['html'].replace(main_css, wooyun_main_css).replace(bootstrap_css, wooyun_bootstrap_css)
            
            if SAVE_IMAGES:
                if item['images']:
                    for it in item['images']:
                            item['html'] = item['html'].replace(it['url'],"../../static/images/" + it['path'])
                    # images = item['images']

            wooyun_knowledge = {                                                          #数据表结构，dictionary型
                    "Title": item['post_title'],
                    "Author": item['post_author'],
                    'Date': item['post_datetime'],
                    'Images' :item['images'],
                    'Content': item['html']
                }

            self.__dbcollection.insert(wooyun_knowledge)
        
        return item

class WooyunImagesPipeline(ImagesPipeline):             #这个ImagePipeline用来下载图片，但下载下来的图片用hash值作为文件名，不是原来的文件名
    def __init__(self,args):
        pass

    def file_path(self, request, info):             #想用这个方法来更改文件名，但未成功，还在查。
        image_guid = request.url.split('/')[-1]
        path = 'full/%s' % (image_guid)
        return path

    def get_media_requests(self, item, info):       #生成图片Request的url
        if SAVE_IMAGES:
            for image_url in item['image_urls']:
                yield Request(image_url)

    def item_completed(self, results, item, info):  #图片下载完成后执行的方法
        if SAVE_IMAGES:
            image_paths = [x['path'] for ok, x in results if ok]
            if not image_paths:
                raise DropItem("Item contains no images")
            item['image_paths'] = image_paths
        return item
