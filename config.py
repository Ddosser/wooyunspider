#!flask/bin/python
#condig:utf-8

from app import app

author = "Ddosser"
version = "1.2"

CSRF_ENABLE = True
SECRET_KEY = "Iowo2utD4czr"
ROWS_PER_PAGE = 15

#Mongodb Connection configure
DB_SERVER = "127.0.0.1"
DB_PORT = 27017
DB_NAME = "wooyun"
DB_COLLECTION_OPENBUG = "wooyuno_penbug"
DB_WOOYUN_OWNER = "wooyun"
DB_WOOYUN_PASSWD = "5fsQgrQSYXg4"
RECORDS_PER_PAGE = 20
DB_PATH = '~/mongodb/data'

app.config['DB_SERVER'] = DB_SERVER
app.config['DB_PORT'] = DB_PORT
app.config['DB_NAME'] = DB_NAME
app.config['DB_COLLECTION_OPENBUG'] = DB_COLLECTION_OPENBUG
app.config['DB_WOOYUN_OWNER'] = DB_WOOYUN_OWNER
app.config['DB_WOOYUN_PASSWD'] = DB_WOOYUN_PASSWD
app.config['RECORDS_PER_PAGE'] = RECORDS_PER_PAGE
app.config['DB_PATH'] = DB_PATH
DB_CONN = {
    "DB_SERVER": app.config['DB_SERVER'],
    "DB_PORT": app.config['DB_PORT'],
    "DB_NAME": app.config['DB_NAME'],
    "DB_OWNER": app.config['DB_WOOYUN_OWNER'],
    "DB_PASSWD": app.config['DB_WOOYUN_PASSWD'],
    "DB_COLLECTION": app.config['DB_COLLECTION_OPENBUG']
}

app.config['DB_CONN'] = DB_CONN
