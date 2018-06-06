#=============================================================
# File Name: unicode_text.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Wed 06 Jun 2018 10:46:10 AM CST
#=============================================================
# coding:utf8

import unicodedata
import sys


s = 'pýtĥöñ\fis\tawesome\r\n'
remap = {
            ord('\t') : ' ',
            ord('\f') : ' ',
            ord('\r') : None # Deleted
        }
a = s.translate(remap)
print(a)
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
print(b)
print(b.translate(cmb_chrs))
