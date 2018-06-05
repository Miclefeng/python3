# zip(dict.values(),dict.keys()).py

prices = {
	'acme':45.23,
	'aapl':612.78,
	'ibm':205.22,
	'hpq':37.20,
	'fb':10.75
}

min_price = min(zip(prices.values(),prices.keys()))
# (10.75, 'fb') 
max_price = max(zip(prices.values(),prices.keys()))
# (612.78, 'aapl')
print(min_price,max_price)

minp = min(prices,key=lambda k:prices[k])
maxp = max(prices,key=lambda k:prices[k])
print(minp,maxp)
# fb aapl

