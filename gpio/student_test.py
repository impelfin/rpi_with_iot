#!/usr/bin/env python

import pymysql 

db=pymysql.connect('localhost','pi','1234','test')
cur=db.cursor()
cur.execute("update student set gender='M' where id<=3")
cur.execute('select * from student')
d =  cur.description
print d[0][0], d[3][0], d[1][0]

while True:
	student = cur.fetchone()
	if not student :
		break
	print(student[0], student[3], student[1])
cur.close()
db.close()
