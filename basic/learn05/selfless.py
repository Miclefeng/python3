# selfless.py
class Selfless:
	def __init__(self,data):
		self.data = data
	def selfless(arg1,arg2):
		return arg1 + arg2
	def normal(self,arg1,arg2):
		return self.data + arg1 + arg2

x = Selfless(2)
print(x.normal(3,4))

print(Selfless.normal(x,3,4))

print(Selfless.selfless(3,4))

#x.selfless(3,4) # x = Selfless(2) 1 param more to given

#Selfless.normal(3,4) # 1 param less to given