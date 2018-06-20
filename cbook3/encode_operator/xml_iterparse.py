#=============================================================
# File Name: xml_iterparse.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Wed 20 Jun 2018 11:02:20 AM CST
#=============================================================
# coding:utf8
from xml.etree.ElementTree import iterparse
from xml.etree.ElementTree import parse
from collections import Counter


def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    # 跳过response的tag
    next(doc)
    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                # 把 start 的 elem 移除出list
                elem_stack[-2].remove(elem)
            try:
                # 把 end 的 elem 移除出list
                tag_stack.pop()
                elem_stack.pop()
            except IndexError as e:
                pass

potholes_by_zip = Counter()
data = parse_and_remove('potholes.xml', 'row/row')
for pothole in data:
    print(pothole.findtext('zip'))

#for zipcode, num in potholes_by_zip.most_common():
#    print(zipcode, num)
