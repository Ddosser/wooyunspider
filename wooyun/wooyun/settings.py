# -*- coding: utf-8 -*-

# Scrapy settings for wooyun project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'wooyun'

IMAGES_STORE = '../app/static/images'             #存放图片的路径
DOWNLOAD_DELAY=1                    #设置下载延迟，为1秒
IMAGES_EXPIRES = 90                 #设置图片过期时间，避免重复下载
IMAGES_MIN_HEIGHT = 110             #以下两项过滤小图片，可根据实际设置
IMAGES_MIN_WIDTH = 110

#Custom settings
SAVE_IMAGES = False                  #设置是否将图片存储到本地，默认为True，即存储图片到本地，如果为False，不存储，同时不更换img src地址
IMAGESPIPELINE_ENABLE = 1           #如果设置了存储图片，则将ImagesPipeline开启，否则关闭
IS_FIRSTTIME_CRAWL = True          #是否是第一次爬取
LOGS_PATH = "./logs/records.log"    #记录每次爬取后的总数，更新爬取参照的变量
RECORDS_PER_PAGE = 20               #页面上每页记录条数

DB_SERVER = "127.0.0.1"                   #mongodb setting
DB_PORT = 27017
DB_NAME = "wooyun"
DB_OWNER = "wooyun"
DB_PASSWD = "5fsQgrQSYXg4"
DB_COLLECTION = "wooyuno_penbug"
DB_PATH = "~/mongodb/data"
MONGODB_CMD = "nohup mongod --dbpath " + DB_PATH + "&"

DB_CONN = {
    "DB_SERVER": DB_SERVER,
    "DB_PORT": DB_PORT,
    "DB_NAME": DB_NAME,
    "DB_OWNER": DB_OWNER,
    "DB_PASSWD": DB_PASSWD,
    "DB_COLLECTION": DB_COLLECTION
}

if not IS_FIRSTTIME_CRAWL:                  #读取上一次记录值
    f = open(LOGS_PATH, "r")
    data = f.readlines()
    for i in range(1, len(data)):
        record = data[-i].replace("\n","").strip().split("|")[0]
        if record:
            OLD_TOTAL_RECORDS = int(record)
            break
        else:
            continue
    f.close()

if not SAVE_IMAGES:
    IMAGESPIPELINE_ENABLE = 0

#End setting
SPIDER_MODULES = ['wooyun.spiders']
NEWSPIDER_MODULE = 'wooyun.spiders'

ITEM_PIPELINES = {
    'wooyun.pipelines.WooyunPipeline': 200,
    'scrapy.pipelines.images.ImagesPipeline': IMAGESPIPELINE_ENABLE,    #开启ImagesPipeline
    'wooyun.pipelines.WooyunImagesPipeline': 300
}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'wooyun (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY=1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
#COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'wooyun.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'wooyun.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'wooyun.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'
