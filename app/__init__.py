#!/usr/bin/evn python
#coding=utf-8
#####################################################
#
#FileName: __init__.py
#Author: arses
#Email: arseswilliam@gmail.com
#Date: 2015-09-19 17:50:31
#
#####################################################

#import flask
from flask import Flask

app = Flask(__name__)

from app import views

