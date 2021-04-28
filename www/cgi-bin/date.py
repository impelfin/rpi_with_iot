#!/usr/bin/python

import time,datetime 

print("Content-type:text/html \r\n\r\n")
print("<html>")
print("<head>")
print("<title>Date CGI Program</title>")
print("</head>")
print("<body>")
print("<H2>Date : %s</H2>" % time.ctime())
time_format = "%a, %d %b %Y %H:%M %S %Z"
print("<H2>Date : %s</H2>" % (datetime.datetime.now().strftime(time_format))) 
print("</body>")
print("</html>")
