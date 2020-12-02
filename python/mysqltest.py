#!/usr/bin/env python

import pymysql 

db=pymysql.connect('localhost','pi','1234','test')
cur=db.cursor()
cur.execute('select * from student')
while True:
	student = cur.fetchone()
	if not student :
		break
	print(student)
cur.close()
db.close()
