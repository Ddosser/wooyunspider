一、项目目标
<<<<<<< HEAD
=======

    收集乌云公开漏洞，提供离线搜索功能，为大家提供学习资源（仅作为学习）。
    
>>>>>>> de920b7684c55ca543961c9e076e57662e36de84

收集乌云公开漏洞，提供在线搜索功能，为大家提供学习资源（仅作为学习）。
二、使用环境

<<<<<<< HEAD
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
三、使用方法

1.设置爬虫选项settengs.py，如果需要全部爬，将IS_FIRST_CRAWL 设置为True，否则设置为False，即只爬更新部分。
2.设置否是将图片保存到本地选项 SAVE_IMAGES
3.设置数据库数据库用户名、密码、数据库名和记录集等。
4.cd到爬虫项目目录，开始爬取
scrapy crawl wooyunspider
5.配置app/config数据库信息，比如数据库服务器地址，端口，数据库名和数据库路径等。
6.开启服务（默认端口为5000）
./run.py
7.用户http://server:5000进行访问。
四、目录结构

wooyunspider
|__run.py
|__config.py
|__README.md
|__wooyun
|    |__logs
|    |__wooyun
|    |__wooyunspider
|    |__scrapy.cfg
|__app
|    |__lib
|    |__static(必须目录)
|    |__templates(必须目录)
|    |__views.py
|__flask
|    |__bin
|    |__include
|    |__lib
|____|__local
五、声明

本项目所收集的漏洞来自乌云，版权及解释权归乌云所有。
项目开发工具均为开源，因此本项目也作为开源供大家使用，但目的只是为大家提供学习资料。
禁止用于非法目的，否则一切后果自负。
=======
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
    
三、使用方法

    1.设置爬虫选项settengs.py，如果需要全部爬，将IS_FIRST_CRAWL 设置为True，否则设置为False，即只爬更新部分。
    2.设置否是将图片保存到本地选项 SAVE_IMAGES
    3.设置数据库数据库用户名、密码、数据库名和记录集等。
    4.cd到爬虫项目目录，开始爬取
    scrapy crawl wooyunspider
    5.配置app/config数据库信息，比如数据库服务器地址，端口，数据库名和数据库路径等。
    6.开启服务（默认端口为5000）
    ./run.py
    7.用户http://server:5000进行访问。
    
四、目录结构

    wooyunspider
    |__run.py
    |__config.py
    |__README.md
    |__wooyun
    |    |__logs
    |    |__wooyun
    |    |__wooyunspider
    |    |__scrapy.cfg
    |__app
    |    |__lib
    |    |__static(必须目录)
    |    |__templates(必须目录)
    |    |__views.py
    |__flask
    |    |__bin
    |    |__include
    |    |__lib
    |____|__local
   
五、声明

    本项目所收集的漏洞来自乌云，版权及解释权归乌云所有。
    项目开发工具均为开源，因此本项目也作为开源供大家使用，但目的只是为大家提供学习资料。
    禁止用于非法目的，否则一切后果自负。
>>>>>>> de920b7684c55ca543961c9e076e57662e36de84
