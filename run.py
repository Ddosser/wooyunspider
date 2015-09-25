#!flask/bin/python
#coding=utf-8
#####################################################
#
#FileName: run.py
#Author: Ddosser
#Email: arseswilliam@gmail.com
#Date: 2015-09-19 17:53:47
#
#####################################################

import os
from app import app
from config import *

#检测mongodb是否开启,如果未开启，则打开，不然无法连接数据库
MONGODB_CMD = "mongod --dbpath " + app.config['DB_PATH'] + "&"
reply = os.popen("ps -ef |grep 'mongod' |awk '{print $8}'").readlines()[0].replace("\n","").strip()
if reply is not "mongod":
    os.system(MONGODB_CMD)
else:
    print "\033[1;32m [*] Mongodb is already runing \033[0m"

app.debug = False 
app.run(host = '0.0.0.0')

