#!/flask/bin/python
#coding:utf-8

import os
import re
import math
import pymongo
from flask import Flask
from bson import ObjectId
from app import app


__author__ = "Ddosser"
__version__ = "1.3"

class DB_Connection(object):
    def __init__(self, db_conn):
        self.__dbconn = db_conn
        self.__database = db_conn['DB_NAME']
        self.__dbclient = pymongo.MongoClient(db_conn['DB_SERVER'], db_conn['DB_PORT'])           #Making a db connection client.
        self.__db = self.__dbclient[db_conn['DB_NAME']]                                          #Sellecting a database (use database)
        self.__db.authenticate(db_conn['DB_OWNER'],db_conn['DB_PASSWD'])
        self.__dbcollection = self.__db[db_conn['DB_COLLECTION']]
        #self.__dbposts = self.__db.posts

    def db_insert(self, db_record):
        try:
            insert_record = self.__dbcollection.insert_one(db_record)
        except:
            pass

    def db_remove(self, record = None):
        if recode:
            res = self.__dbcollection.remove(record)
        else:
            res = self.__dbcollection.remove()
        if res["n"] == 1:
            print "[*]remove {} from {} ok!".format(recode, self.__database)
        else:
            print "[*]remove {} from {} Failed!".format(recode, self.__database)

    def db_query(self, fieldname = None, keywords = None , page = 1):
        total_page = 0
        total_rows = 0
        page = page
        keyword_regex = {}
        k = keywords.split(" ")
        keyword_list = [kw for kw in k if kw!=""]
        if not len(keyword_list):
            page_info = None
            return page_info

        reg_pattern = re.compile('|'.join(keyword_list), re.IGNORECASE)
        keyword_regex[fieldname] = reg_pattern

        total_rows = self.__dbcollection.find(keyword_regex).count()
        total_page = int(math.ceil(total_rows / (app.config['RECORDS_PER_PAGE']*1.0)))
        page_info = {
            "keyword":keywords,
            "totalpage":total_page,
            "records":total_rows,
            "currentpage":page,
            'rows':[]
        }
        if total_page >0 and page <= total_page:
            row_start = (page - 1) * app.config['RECORDS_PER_PAGE']
            if self.__dbconn['DB_COLLECTION'] == app.config['DB_COLLECTION_OPENBUG']:
                cursors = self.__dbcollection.find(keyword_regex, {'WooyunID':1, 'Title':1, 'Open Time':1, 'Date':1, 'Author':1, 'Vul_Type':1})\
                .sort('Open Time',pymongo.DESCENDING).skip(row_start).limit(app.config['RECORDS_PER_PAGE'])
            elif self.__dbconn['DB_COLLECTION'] == app.config['DB_COLLECTION_KNOWLEDGE']:
                cursors = self.__dbcollection.find(keyword_regex, {'_id':1, 'Title':1, 'Date':1, 'Author':1})\
                .sort('Date',pymongo.DESCENDING).skip(row_start).limit(app.config['RECORDS_PER_PAGE'])
            for c in cursors:
                page_info['rows'].append(c)
        return page_info

    def db_queryone(self, fieldname = None, keywords = None):
        keyword_regex = {}
        k = keywords.split(" ")
        keyword_list = [kw for kw in k if kw!=""]
        reg_pattern = re.compile('|'.join(keyword_list), re.IGNORECASE)
        keyword_regex[fieldname] = reg_pattern
        if self.__dbconn['DB_COLLECTION'] == app.config['DB_COLLECTION_KNOWLEDGE']:
            res = self.__dbcollection.find_one({"_id":ObjectId(keywords.strip())}, {'_id':0, 'Title':1, 'Date':1, 'Author':1, 'Content':1})
        elif self.__dbconn['DB_COLLECTION'] == app.config['DB_COLLECTION_OPENBUG']:
            res = self.__dbcollection.find_one(keyword_regex, {'_id':0, 'WooyunID':1, 'Title':1, 'Open Time':1, 'Date':1, 'Author':1, 'Vul_Type':1, 'Content':1})
        else:
            res = None
        return res

    def db_close(self):
        self.__client.close()

def main():
    try:
        db_conn = app.config['DB_CONN']
    except:
        db_conn = DB_CONN
    conn = DB_Connection(db_conn)

    data = conn.db_query("sql")
    for res in data['rows']:
        print res['WooyunID']

if __name__ == '__main__':
    main()

