#=============================================================
# File Name: update_xml.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Thu 21 Jun 2018 10:02:47 AM CST
#=============================================================
# coding:utf8
from xml.etree.ElementTree import parse, Element


doc = parse('pred.xml')
root = doc.getroot()

root.remove(root.find('cr'))
index = root.getchildren().index(root.find('nm'))
print(index)
e = Element('spam')
e.text = 'Miclefeng zss'
root.insert(2, e)
doc.write('pred.xml', xml_declaration=True)
