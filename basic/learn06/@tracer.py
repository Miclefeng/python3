# tracer.py
class tracer:
	def __init__(self,func):
		self.calls = 0
		self.func = func
	def __call__(self,*args,**kargs):
		self.calls += 1
		print('call %s to %s' % (self.calls,self.func.__name__))
		return self.func(*args,**kargs)

@tracer
def spam(a,b,c):
	print(a + b + c)

@tracer
def eggs(x,y):
	print(x ** y)
spam(1,2,3)
# call 1 to spam
# 6
spam(a=4,b=5,c=6)
# call 2 to spam
# 15
print('-'*20)
eggs(2,16)
# call 1 to eggs
# 65536
eggs(4,y=4)
# call 2 to eggs
# 256



