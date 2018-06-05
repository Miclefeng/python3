# super.py

class Super:
	def method(self):
		print('in Super.method')

class Sub(Super):
	def method(self):
		print('starting Sub.method')
		Super.method(self)
		print('ending Sub.method')

x = Super()
x.method()
print('\n')
x = Sub()
x.method()
