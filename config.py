#!flask/bin/python
#condig:utf-8

from app import app

__author__ = "Ddosser"
__version__ = "1.3"

CSRF_ENABLE = True
SECRET_KEY = "Iowo2utD4czr"
#ROWS_PER_PAGE = 15

#Mongodb Connection configure
DB_SERVER = "192.168.0.19"								#databases server
DB_PORT = 27017										#databases server port
DB_NAME = "wooyun"									#databases name
DB_COLLECTION_OPENBUG = "wooyun_openbug"			#Open  Bugs Databases Collection
DB_COLLECTION_KNOWLEDGE = "wooyun_knowledge"		#Knowledge Databases Collection
DB_WOOYUN_OWNER = "wooyun"							#User
DB_WOOYUN_PASSWD = "5fsQgrQSYXg4"					#Password
RECORDS_PER_PAGE = 20	
DB_PATH = '~/mongodb/data'							#databases path


app.config['DB_SERVER'] = DB_SERVER
app.config['DB_PORT'] = DB_PORT
app.config['DB_NAME'] = DB_NAME
app.config['DB_COLLECTION_OPENBUG'] = DB_COLLECTION_OPENBUG
app.config['DB_WOOYUN_OWNER'] = DB_WOOYUN_OWNER
app.config['DB_WOOYUN_PASSWD'] = DB_WOOYUN_PASSWD
app.config['RECORDS_PER_PAGE'] = RECORDS_PER_PAGE
app.config['DB_PATH'] = DB_PATH

#wooyun knowledge
app.config['DB_COLLECTION_KNOWLEDGE'] = DB_COLLECTION_KNOWLEDGE

DB_CONN = {
    "DB_SERVER": app.config['DB_SERVER'],
    "DB_PORT": app.config['DB_PORT'],
    "DB_NAME": app.config['DB_NAME'],
    "DB_OWNER": app.config['DB_WOOYUN_OWNER'],
    "DB_PASSWD": app.config['DB_WOOYUN_PASSWD'],
    "DB_COLLECTION": app.config['DB_COLLECTION_OPENBUG']
}

app.config['DB_CONN'] = DB_CONN
