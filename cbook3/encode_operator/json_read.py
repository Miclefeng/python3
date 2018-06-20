#=============================================================
# File Name: json_read.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Tue 19 Jun 2018 03:07:17 PM CST
#=============================================================
# coding:utf8
import json
from urllib.request import urlopen
from urllib.parse import quote
from pprint import pprint
import string


data = {
        'name' : 'ACME',
        'shares' : 100,
        'price' : 542.23
       }

with open('data.json', 'w') as f:
    json.dump(data, f)

with open('data.json', 'r') as f:
    print(json.load(f))

url = 'http://t.yushu.im/v2/book/search?q=程序员的数学&count=10&start=0'
u = urlopen(quote(url, safe=string.printable, encoding='utf-8'))
resp = json.loads(u.read().decode('utf-8'))
pprint(resp)
