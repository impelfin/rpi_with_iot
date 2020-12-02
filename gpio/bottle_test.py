#!/usr/bin/python

import bottle
import bottle_mysql

app = bottle.Bottle()
plugin = bottle_mysql.Plugin(dbuser='pi',dbpass='1234',dbname='test')
app.install(plugin)

@app.route('/show/<item>')
def show(item, db):
	db.execute('select * from sutdent where gender="%s"',(item,))
	row = db.fetchone()
	if row:
		return template('showitem',page=row)
	return HTTPError(404,"Page not found")	

run(host='192.168.10.11', port=8000, debug=True)
