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

from flask import render_template
from flask import redirect
from flask import flash
from flask import request

from app import app
from lib.dbconn import DB_Connection
from forms import SearchForm
#from flask.ext.pymongo import PyMongo

result = None

@app.route('/')
@app.route('/index', methods = ["GET"])
def index():
    return render_template('index.html',
    title = "Welcome to Hacker's World",)

@app.route('/search', methods = ["GET", "POST"])
def search():
    global result
    title = "Search Result"
    search = None
    conn = DB_Connection("wooyun")
    if request.method == "GET":
        return render_template('index.html',
        title = "Welcome to Hacker's World",)
    search = request.form['WooyunBug']
    if not search:
        return render_template('index.html',
        title = "Welcome to Hacker's World",)
    res = conn.db_query(search)
    if not res:
        return render_template('index.html',
        title = "Welcome to Hacker's World",)
    result = res
    return render_template('search.html',
    title = title.encode('utf-8'), search = search, data = res)
    conn.db_close()

@app.route('/detail/<cid>', methods = ['GET'])
def detail(cid):
    conn = DB_Connection("wooyun")
    result = conn.db_queryone(str(cid))
    if not result:
        return render_template('index.html',
        title = "Welcome to Hacker's World",)      
    return(result['Content'])
    conn.db_close()

