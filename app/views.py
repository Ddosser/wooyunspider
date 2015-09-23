#!/flask/bin/python
#coding=utf-8
#####################################################
#
#FileName: views.py
#Author: Ddosser
#Email: arseswilliam@gmail.com
#Date: 2015-09-19 17:51:43
#
#####################################################

import math
import pymongo
from flask import render_template
from flask import redirect
from flask import flash
from flask import request
from flask import url_for
from flask import Flask
from app import app
from lib.dbconn import DB_Connection
#from forms import SearchForm

author = "Ddosser"
version = "v1.2"

@app.route('/')
@app.route('/index', methods = ["GET"])
def index():
    return render_template('index.html',
    title = "Welcome to Hacker's World",)

@app.route('/search', methods = ["GET", "POST"])
def search():
    title = "Search Result"
    keywords = None
    conn = DB_Connection(app.config['DB_CONN'])

    if request.method == "POST":
        keywords = request.form['WooyunBug']
        page = 1

    if request.method == "GET" :
        keywords = request.args.get('keywords')
        page = int(request.args.get('page',1))
        if page < 1: page = 1

    if not keywords:
        return redirect(url_for('index'))
        #pass

    page_info = conn.db_query(fieldname = "Title", keywords = keywords, page = page)

    return render_template('search.html',\
                                    title = title.encode('utf-8'),\
                                    page_info = page_info
                        )
    conn.db_close()

#return WooyunBug page
@app.route('/<cid>', methods = ['GET'])
def detail(cid):
    conn = DB_Connection(app.config['DB_CONN'])
    result = conn.db_queryone(fieldname = 'WooyunID', keywords = str(cid))
    if not result:
        return render_template('index.html',
        title = "Welcome to Hacker's World",)
    return(result['Content'])
    conn.db_close()
