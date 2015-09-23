一、项目目标
    收集乌云公开漏洞，提供在线搜索功能，为大家提供学习资源（仅作为学习）。

二、使用环境
    1.本项目在Ubuntu上开发，依赖于python2.7。
    sudo apt-get install python
    2.使用scrapy爬虫框架
    sudo apt-get install python-scrapy   or sudo pip install scrapy
    3.使用数据库为mongodb，包依赖pymongo
    sudo apt-get install python-pymongo  or sudo pip install pymongo
    4.服务器端采用Flask，安装相关的包:
    sudo apt-get install virtualenv
    sudo apt-get install python-flask    or sudo pip install flask
    5.前端采用bootstrap v3版，下载地址：
    http://v3.bootcss.com/getting-started/#download
三、目录结构
    wooyunspider
    |__run.py
    |__config.py
    |__wooyun
    |  |__logs
    |  |__wooyun
    |  |__wooyunspider
    |  |__scrapy.cfg
    |__app
    |   |__lib
    |   |__static
    |   |__templates
    |___|__views.py
   
四、声明
   本项目所收集的漏洞来自乌云，版权及解释权归乌云所有。项目开发工具均为开源，因此本项目也作为开源供大家使用，但项目的目的只是为大家提供学习资料
禁止用于非法目的，否则一切后果自负。
