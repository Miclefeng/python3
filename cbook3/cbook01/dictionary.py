# dictionary.py
prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }
p1 = {key:value for key,value in prices.items() if value > 200}
print(list(p1))			# ['IBM', 'AAPL']


tech_names = {'AAPL','IBM','HPQ','MSFT'}
p2 = {key:value for key,value in prices.items() if key in tech_names}
print(list(p2))			# ['IBM', 'AAPL', 'HPQ']