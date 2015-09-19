#!/usr/bin/env python
#coding:utf-8

import os
import pymongo


author = "ddosser"
version = "1.0"

class DB_Connection(object):
    def __init__(self, database):
        self.__db_host = "127.0.0.1"
        self.__db_port = 27017
        self.__database = database
        self.__db_posts = ""
        self.__db_init()

    def __db_init(self):
        _client = pymongo.MongoClient(self.__db_host, self.__db_port)            #Making a db connection client.
        _db = _client[self.__database]                    #Sellecting a database (use database)
        _db.authenticate("wooyun","5fsQgrQSYXg4")
        self.__db_posts = _db.posts
        self.__db_collection = _db[self.__database]

    def db_insert(self, post):
        try:
            _posts_id = self.__db_posts.insert_one(post)
        except:
            pass

    def db_remove(self, post = None):
        if post:
            res = self.__db_posts.remove(post)
        else:
            res = self.__db_posts.remove()
        if res["n"] == 1:
            print "[*]remove {} from {} ok!".format(post, self.__database)
        else:
            print "[*]remove {} from {} Failed!".format(post, self.__database)

    def db_query(self, post = None):
        if post:
            search = {'Content':{'$regex':post} }
            res = self.__db_posts.find(search)
        return res
            #res = self._db_posts.find(post)
def save_html(data, i):
	f = open("/home/arses/Python/wooyun/test/index" + str(i) + ".html", "a")
	if data:
		f.write(data)
	f.close()

def main():
    db_name = "wooyun"
    conn = DB_Connection(db_name)
    flag = 1
    q = "话说联系方式都要了"
    i = 0
    for data in conn.db_query(q):
    	i += 1
    	print data[u'Content'].encode('utf-8')
    	#save_html(data[u'Content'].encode('utf-8'), i)
    conn.db_remove()
    print i
    
if __name__ == '__main__':
    main()

