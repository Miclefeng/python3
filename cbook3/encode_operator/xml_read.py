#=============================================================
# File Name: xml_read.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Tue 19 Jun 2018 03:52:28 PM CST
#=============================================================
# coding:utf8
from urllib.request import urlopen
from xml.etree.ElementTree import parse


u = urlopen('https://m.huanqiu.com/rss')
doc = parse(u)

for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')
    print(title)
    print(date)
    print(link)
    print()
