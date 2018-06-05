# decorator01.py
class tracer:
	def __init__(self,func):
		self.calls = 0
		self.func = func
	def __call__(self,*args):
		self.calls += 1
		print('call %s to %s' % (self.calls,self.func.__name__))
		self.func(*args)  # doit spam(a,b,c)

@tracer
def spam(a,b,c):
	print(a + b +c)

spam(1,2,3)
# call 1 to spam
# 6
spam('a','b','c')
# call 2 to spam
# abc
print(spam.calls)
# 2
print(spam)
# <__main__.tracer object at 0x7f245aeb9940>

print('-' * 30)

calls = 0

def tracer(func,*args):
	global calls
	calls += 1
	print('call %s to %s' % (calls,func.__name__))
	func(*args)
def spam(a,b,c):
	print(a,b,c)

spam(1,2,3)
# 1 2 3
tracer(spam,1,2,3)
# call 1 to spam
# 1 2 3
print(calls) # 1




