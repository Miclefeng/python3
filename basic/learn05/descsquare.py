# descsquare.py
class DescSquare:
	def __init__(self,start):
		self.value = start
	def __get__(self,instance,owner):
		return self.value ** 2
	def __set__(self,instance,value):
		self.value = value

class Client1:
	x = DescSquare(3)

class Client2:
	x = DescSquare(32)

c1 = Client1()
c2 = Client2()

print(c1.x)		# 9
c1.x = 4
print(c1.x)		# 16
print(c2.x)		# 1024



