#square.py
def square(arg):
	return arg ** 2

class Sum:
	def __init__(self,val):
		self.val = val
	def __call__(self,arg):
		return self.val + arg

class Product:
	def __init__(self,val):
		self.val = val
	def method(self,arg):
		return self.val * arg

sobject = Sum(2)
pobject = Product(3)
actions = [square,sobject,pobject.method]

for act in actions:
	print(act(5))

print(list(map(lambda act: act(5),actions)))
print([act(5) for act in actions])
