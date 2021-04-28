#!/usr/bin/env python

def application(environ, start_response):
	status = '200 OK'
	output = 'Hello WSGI'
	response_headers = [('Content-type','text/plain'), ('Content-Length',str(len(output)))]
	start_response(status, response_headers)
	return [output]

if __name__=='__main__':
	from flup.server.fcgi import WSGIServer
	WSGIServer(application).run()
