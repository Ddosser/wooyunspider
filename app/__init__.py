#!flask/bin/python
#coding=utf-8
#####################################################
#
#FileName: __init__.py
#Author: Ddosser
#Email: arseswilliam@gmail.com
#Date: 2015-09-19 17:50:31
#
#####################################################

from flask import Flask


app = Flask(__name__)
app.config.from_object(__name__)
from app import views
