#!/usr/bin/env python

from bottle import route, run, request, response 

@route('/')
def hello_world():
	return 'Hello World!'

@route('/hello')
def hello_again():
	if request.get_cookie('Visited'):
		return 'Welcome back! Nice to see you again'
	else:
		response.set_cookie('Visited', 'yes')
		return 'Hello there! Nice to meet you'

run(host='192.168.10.11', port=8000, debug=True)
