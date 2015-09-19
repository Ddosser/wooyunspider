#!/flask/bin/python
#coding=utf-8
#####################################################
#
#FileName: views.py
#Author: arses
#Email: arseswilliam@gmail.com
#Date: 2015-09-19 17:51:43
#
#####################################################

from app import app

@app.route('/')
@app.route('/index')

def index():
    return "hello world!\n"

