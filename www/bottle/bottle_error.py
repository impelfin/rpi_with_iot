#!/usr/bin/env python

from bottle import route, run, error, abort

@route('/')
def hello_world():
	return 'Hello World!'

@error(404)
def error404(error):
	return 'This page is not existed.'

@route('/wrong')
def wrong():
	abort(401, 'Sorry, That page is not existed.')	

run(host='192.168.10.11', port=8000, debug=True)
