# decorator.py
def decorator(cls):
	class Wrapper:
		def __init__(self,*args):
			self.wrapped = cls(*args)
			print(self.wrapped)		#<__main__.C object at 0x7ff8a84c9a90>

		def __getattr__(self,name):
			return getattr(self.wrapped,name)
	return Wrapper

@decorator
class C:
	def __init__(self,x,y):
		self.attr = 'spam'

x = C(6,7)
print(x.attr)		# spam
