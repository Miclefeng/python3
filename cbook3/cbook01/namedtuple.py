# namedtuple.py
from collections import namedtuple

subscriber = namedtuple('subscriber',['addr','joined'])
sub = subscriber('jonesy@example.com','2012-10-19')
print(sub)
# subscriber(addr='jonesy@example.com', joined='2012-10-19')
print(sub.addr)		# jonesy@example.com
print(sub.joined)	# 2012-10-19

def compute_cost(records):
	total = 0.0
	for rec in records:
		s = Stock(*rec)
		total += s.shares * s.price
	return total
Stock = namedtuple('Stock',['name','shares','price'])
s = Stock('ACME',100,123.45)
print(s)	# Stock(name='ACME', shares=100, price=123.45)

s = s._replace(shares=75,price=110)
print(s)	# Stock(name='ACME', shares=100, price=110)

stock2 = namedtuple('stock2',['name','shares','price','date','time'])
stock_property = stock2('',0,0.0,None,None)

def dict_to_stock(s):
	return stock_property._replace(**s)
a = {'name':'ACME','shares':100,'price':123.45}
print(dict_to_stock(a))
# stock2(name='ACME', shares=100, price=123.45, date=None, time=None)
b = {'name':'WOW','shares':696,'price':20,'date':2005,'time':'5 years'}
print(dict_to_stock(b))
# stock2(name='WOW', shares=696, price=20, date=2005, time='5 years')


