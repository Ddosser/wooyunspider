#!/usr/bin/env python
#coding:utf-8

import os
import re
import math
import pymongo


author = "ddosser"
version = "1.0"

class DB_Connection(object):
    def __init__(self, database):
        self.__dbhost = "127.0.0.1"
        self.__dbport = 27017
        self.__database = database
        self.__db_init()

    def __db_init(self):
        client = pymongo.MongoClient(self.__dbhost, self.__dbport)            #Making a db connection client.
        db = client[self.__database]                    #Sellecting a database (use database)
        db.authenticate("wooyun","5fsQgrQSYXg4")
        self.__dbcollection = db["wooyun_openbug"]

    def db_insert(self, post):
        try:
            _posts_id = self.__db_posts.insert_one(post)
        except:
            pass

    def db_remove(self, post = None):
        if post:
            res = self.__dbcollection.remove(post)
        else:
            res = self.__dbcollection.remove()
        if res["n"] == 1:
            print "[*]remove {} from {} ok!".format(post, self.__database)
        else:
            print "[*]remove {} from {} Failed!".format(post, self.__database)

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
        total_page = int(math.ceil(total_rows / (20*1.0)))
        page_info = {
            "keyword":keywords,
            "totalpage":total_page,
            "records":total_rows,
            "currentpage":page,
            'rows':[]
        }

        if total_page >0 and page <= total_page:
            cursors = self.__dbcollection.find(keyword_regex, {'WooyunID':1, 'Title':1, 'Open Time':1, 'Date':1, 'Author':1, 'Vul_Type':1})\
                .sort('Open Time',pymongo.DESCENDING).limit(20)
            for c in cursors:
                page_info['rows'].append(c)
        return page_info

def save_html(data, i):
	f = open("/home/arses/Python/wooyun/test/index" + str(i) + ".html", "a")
	if data:
		f.write(data)
	f.close()

def main():
    db_name = "wooyun"
    conn = DB_Connection(db_name)
    flag = 1
    q = "SQL"
    i = 0

    # for data in conn.db_query(q):
    # 	# i += 1
    # 	# print data[u'Content'].encode('utf-8')
    #  #    print i
    print conn.db_query("Title", keywords = q, page = 2)
    	#save_html(data[u'Content'].encode('utf-8'), i)
    #conn.db_remove()
    
    
if __name__ == '__main__':
    main()

