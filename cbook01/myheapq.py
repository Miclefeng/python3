# heapq.py
import heapq
nums = [1,3,6,4,16,66,88,99,0,-66]
print(heapq.nlargest(3,nums))
# [99, 88, 66]
print(heapq.nsmallest(3,nums))
# [-66, 0, 1]
portfolio = [{'name':'IBM','shares':100,'price':91.1},
		{'name':'AAPL','shares':50,'price':543.22},
		{'name':'FB','shares':200,'price':21.09},
		{'name':'HPQ','shares':35,'price':31.75},
		{'name':'YHOO','shares':45,'price':16.35},
		{'name':'ACME','shares':75,'price':115.65}]

cheap = heapq.nsmallest(3,portfolio,key=lambda s:s['price'])		
expensive = heapq.nlargest(3,portfolio,key=lambda s:s['price'])
print(cheap)
# [{'name': 'YHOO', 'price': 16.35, 'shares': 45}, {'name': 'FB', 'price': 21.09, 'shares': 200}, {'name': 'HPQ', 'price': 31.75, 'shares': 35}]
print(expensive)
# [{'name': 'AAPL', 'price': 543.22, 'shares': 50}, {'name': 'ACME', 'price': 115.65, 'shares': 75}, {'name': 'IBM', 'price': 91.1, 'shares': 100}]

