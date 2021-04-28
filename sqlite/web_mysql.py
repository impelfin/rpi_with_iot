#!/usr/bin/env python

from bottle import *
from bottle_mysql import Plugin 

mysql = Plugin(user='pi',dbpass='1234',dbname='test')
install(mysql)

@route('/show')
def show(db):
	row = db.execute("select * from student")
	if row:
		return template('showitem', items=row)
	return HTTPError(404,"Page is not found.")

@route('/show/<item>')
def show(item, db):
	row = db.execute("select * from student where name like ?",(item,)).fetchall()
	if row:
		return template('showitem', items=row)
	return HTTPError(404,"Page is not found.")
run(host='192.168.10.11',port=8000,debug=True)
