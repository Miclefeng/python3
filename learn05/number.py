# number.py

class Number:
	def __init__(self,start):
		self.data = start
	def __sub__(self,other):
		return Number(self.data - other)

x = Number(5)
print(x.data)
y = x - 2
print(y.data)