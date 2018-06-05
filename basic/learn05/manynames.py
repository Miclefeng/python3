# manynames.py
x = 11
def f():
	print(x)

def g():
	x = 22
	print(x)

class C:
	x = 33
	def m(self):
		x = 44
		print(x)
		self.x = 55

f()
g()
z = C()
print(z.x)
z.m()
print(z.x)
