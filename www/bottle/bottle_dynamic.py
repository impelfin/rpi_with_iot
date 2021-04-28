#!/usr/bin/env python

from bottle import route, run, static_file

@route('/object/<id:int>')
def callback(id):
	assert isinstance(id, int)

@route('/show/<name:re:[a-p]+>')
def callback(name):
	assert name.isalpha()

@route('/static/<filename:re:.*.png>')
def static(filename):
	return static_file(filename, root='/home/pi/python/')

@route('/download/<filename:re:.*.png>')
def download(filename):
	return static_file(filename, root='/home/pi/python/',download=filename)

run(host='192.168.10.11', port=8000, debug=True)
