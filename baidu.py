# -*- coding:utf-8 -*-
import requests
import re
import time
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def getfromBaidu(word):
    listArray=[]
    list = []
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, compress',
        'Accept-Language': 'en-us;q=0.5,en;q=0.3',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
        }
    baiduurl = 'http://www.baidu.com'
    url = 'http://www.baidu.com.cn/s?wd=' + word + '&cl=3'
    html = requests.get(url=url,headers=headers)
    path = etree.HTML(html.content)
    #用k来控制爬取的页码范围
    for k in range(1, 60):
        path = etree.HTML(requests.get(url, headers).content)
        flag = 11
        if k == 1:
            flag = 10
        for i in range(1, flag):
            sentence = ""
            for j in path.xpath('//*[@id="%d"]/h3/a//text()'%((k-1)*10+i)):
                sentence+=j
            line = ''.join(sentence.strip().split())
            searchObj = re.search( r'\d+(\.\d+)+', line, re.M|re.I)
            if searchObj:
                searchString =  "" + searchObj.group()
                print searchString
                listArray.append(searchString)
        url = baiduurl+path.xpath('//*[@id="page"]/a[%d]/@href'%flag)[0]
    # 去重
    list = set(listArray)
    return list

#主程序测试函数
if __name__ == '__main__':
    start_time = time.time() # 开始时间
    with open('data.txt','wa') as f:
         result = getfromBaidu('Serv-U')
         print len(result)
         for item in result:
             f.writelines(item+ '\n')
         end_time = time.time() #结束时间
         print("程序耗时%f秒." % (end_time - start_time))
