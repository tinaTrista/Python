# -*- coding:utf-8 -*-
#!/usr/bin/python
import re

line = "serveru|serv-uV6.0.0.2破解版下载_完美软件下载";

searchObj = re.search( r'\d+(\.\d+)*', line, re.M|re.I)

#r'(v|V){1}\d+(\.\d+)*',
if searchObj:
   print "searchObj.group() : ", searchObj.group()
else:
   print "Nothing found!!"
