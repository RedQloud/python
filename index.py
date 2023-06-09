#!python
# -*- coding: utf-8 -*-

print("Content-Type: text/html")
print()

import cgi
import cgi, os

files = os.listdir('data')
listStr = ''
for item in files:
    listStr += '<li><a href="index.py?id={}">{}</a></li>'.format(item,item)

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello, web'
    
print('''
  <!doctype html>
  <html>
  
  <head>
    <title>WEB1 - Welcome</title>
  </head>
  
  <body>
    <h1><a href="index.py">WEB</a></h1>
    <ol>
        {listStr}
    </ol>
    <h2>{title}</h2>
    <p>{desc}</p>
  </body>
  
  </html>
'''.format(title=pageId, desc=description, listStr=listStr))
