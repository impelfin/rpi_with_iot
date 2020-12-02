#!/usr/bin/node

var http = require('http')

http.createServer(function (request, response) {
	response.writeHead(200, {'Content-Type':'text/plain'});
	response.end('Hello World\n');
}).listen(1337, '192.168.10.11');

console.log('Server running at http://192.168.10.11:1337');
