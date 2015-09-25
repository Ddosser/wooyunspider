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
SEARCHWHAT = None
@app.route('/')
@app.route('/index', methods = ["GET"])
def index():
    return render_template('index.html',
    title = "Welcome to Hacker's World", index = True)

# @app.route('/openbug', methods = ["GET", "POST"])
@app.route('/search', methods = ["GET", "POST"])
def search():
    title = "Search Result"
    global SEARCHWHAT
    keywords = None
    #conn = DB_Connection(app.config['DB_CONN'])

    if request.method == "POST":
        keywords = request.form['keywords']
        SEARCHWHAT = request.form['searchwhat']
        page = 1
        if SEARCHWHAT == "knowledge":
            app.config['DB_CONN']["DB_COLLECTION"] = app.config['DB_COLLECTION_KNOWLEDGE']
        else:
            app.config['DB_CONN']["DB_COLLECTION"] = app.config['DB_COLLECTION_OPENBUG']
        
    if request.method == "GET" :
        keywords = request.args.get('keywords')
        page = int(request.args.get('page',1))
        SEARCHWHAT = request.args.get('searchwhat')
        if page < 1: page = 1
        if SEARCHWHAT == "knowledge":
            app.config['DB_CONN']["DB_COLLECTION"] = app.config['DB_COLLECTION_KNOWLEDGE']
        else:
            app.config['DB_CONN']["DB_COLLECTION"] = app.config['DB_COLLECTION_OPENBUG']    

    if not keywords:
        return redirect(url_for('index'))
        #pass
    conn = DB_Connection(app.config['DB_CONN'])
    page_info = conn.db_query(fieldname = "Title", keywords = keywords, page = page)

    return render_template('search.html',\
                    title = title.encode('utf-8'),\
                    page_info = page_info,
                    searchwhat = SEARCHWHAT
                )
    conn.db_close()

#return WooyunBug page
@app.route('/<cid>', methods = ['GET'])
def detail(cid):
    global SEARCHWHAT
    if SEARCHWHAT == "knowledge":
        app.config['DB_CONN']["DB_COLLECTION"] = app.config['DB_COLLECTION_KNOWLEDGE']
        fieldname = '_id'
    else:
        app.config['DB_CONN']["DB_COLLECTION"] = app.config['DB_COLLECTION_OPENBUG']
        fieldname = "WooyunID"
    conn = DB_Connection(app.config['DB_CONN'])
    result = conn.db_queryone(fieldname = fieldname, keywords = str(cid))
    if not result:
        return redirect(url_for('index'))
    return(result['Content'])
    conn.db_close()
