#!/usr/bin/env python

from time import sleep
from bottle import route, run, redirect, get, post, request

@route('/')
def hello():
	sleep(2)
	redirect('/login')
@get('/login')
def login():
	return '''
	<form action='login' method='post'>
		Username : <input name='username' type='text' />
		Password : <input name='password' type='password' />
		<input value='Login' type='submit' />
	</form>
	'''
def check_login(username, password):
	f = open('data.txt', 'r')
	line = f.readline()
	login_info  = line.split('/')
	if username==login_info[0] and password==login_info[1]:
		return True
	else:
		return False
	f.close()
	
@post('/login')
def do_login():
	username=request.forms.get('username')
	password=request.forms.get('password')
	if check_login(username, password):
		return '<p> Your login information was correct.</p>'
	else:
		return '<p> Login Failed.</p>'
run(host='192.168.10.11',port=8000,debug=True)
