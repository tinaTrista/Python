#coding=utf-8
import urllib2
import urllib
from bs4 import BeautifulSoup
import sys
import re

with open('data.txt','wa') as f:
    key_word = []
    with open('key_word.txt','r') as kf:
        for line in kf:
            request = urllib2.Request('http://www.baidu.com/s?wd='+urllib.quote(line.strip().decode(sys.stdin.encoding).encode('gbk')))
            response = urllib2.urlopen(request)

            soup = BeautifulSoup(response.read())

            data = [re.sub(u'<[\d\D]*?>',' ',str(item)) for item in soup.select('div.result h3.t > a')]

            for item in data:
                f.writelines(''.join(item.strip().split())+'\n')
