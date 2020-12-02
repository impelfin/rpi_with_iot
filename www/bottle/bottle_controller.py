#!/usr/bin/env python 

import bottle

mythings=['apple','orange','banana','peach']

@bottle.route('/')
def home_page():
	fruit=bottle.request.get_cookie('fruit')
	return bottle.template('hello_world',username='raspberry', things=mythings,like=fruit)
@bottle.post('/favorite_fruits')
def favorite_fruits():
	fruit=bottle.request.forms.get('fruit')
	if(fruit==None or fruit==""):
		fruit='No fruit selected'
	bottle.response.set_cookie('fruit',fruit)
	return bottle.template('fruit.tpl',{'fruit':fruit})

bottle.run(host='192.168.10.11', port=8000, debug=True)
