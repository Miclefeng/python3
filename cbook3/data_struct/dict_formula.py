#=============================================================
# File Name: dict_formula.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Mon 04 Jun 2018 06:02:06 PM CST
#=============================================================
# coding:utf8

prices = {
            'ACME': 45.23,
            'AAPL': 612.78,
            'IBM': 205.55,
            'HPQ': 37.20,
            'FB': 10.75
         }

print('prices > 200 dict :')
p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)

tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
print("\npirces in tech_names dict :")
p2 = {key: value for key, value in prices.items() if key in tech_names}
print(p2)
