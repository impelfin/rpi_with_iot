#!/usr/bin/env python

from bottle import route, run

@route('/')
def home():
	return 'Hello Bottle Home page'

@route('/<name>')
def index(name='World'):
	return 'Hello %s!' % name

run(host='192.168.10.11', port=8000)
