#!/usr/bin/env python

from bottle import route, run

@route('/')
def hello_world():
	return 'Hello World!'
@route('/how')
def how():
	return 'Hello, How are you?'

@route('/hello/<name>')
def hello_name(name):
	return 'Hello, %s!' % name

run(host='192.168.10.11', port=8000, debug=True)
