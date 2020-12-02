#!/usr/bin/python3

import pymysql

db = pymysql.connect(host='localhost', port=8080, user='pi', passwd='1234', db='test',charset='utf8')

cursor = db.cursor()

sql = """ select * from student; """

cursor.execute(sql)

result = cursor.fetchall()

