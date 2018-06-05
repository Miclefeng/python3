# nameinstance.py

class Name:
	"name descriptor docs"
	def __get__(self,instance,owner):
		print('fetch...')
		return instance._name
	def __set__(self,instance,value):
		print('change...')
		instance._name = value
	def __delete__(self,instance):
		print('remove...')
		del instance._name 

class Person:
	def __init__(self,name):
		self._name = name
		print(name+'+++++++')
	name = Name()
	print(name)

bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name
print('-' * 30)
sue = Person('Sue Jones')
print(sue.name)
print(Name.__doc__)
# <__main__.Name object at 0x7f8f872729e8>
# Bob Smith+++++++
# fetch...
# Bob Smith
# change...
# fetch...
# Robert Smith
# remove...
# ------------------------------
# Sue Jones+++++++
# fetch...
# Sue Jones
# name descriptor docs
