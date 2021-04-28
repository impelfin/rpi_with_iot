#!/usr/bin/python

import cgi, cgitb

form = cgi.FieldStorage()

login_id = form.getvalue('loginid')
password = form.getvalue('password')

print("Content-type:text/html \r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Login CGI Program</title>")
print("</head>")
print("<body>")
print("<H2>Hello %s</H2>" % (login_id))
print("</body>")
print("</html>")
