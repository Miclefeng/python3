# supperperson.py
# class Supper:
# 	def __init__(self,name):
# 		self._name = name
# 	name = Name()

# class Person1(Supper): pass


class Person:
	def __init__(self,name):
		self._name = name

	class Name:
		"name descriptor docs"
		def __get__(self,instance,owner):
			print('Fetch...')
			return instance._name
		def __set__(self,instance,value):
			print('Change...')
			instance._name = value
		def __delete__(self,instance):
			print('Remove...')
			del instance._name
	name = Name()

print(Person.Name.__doc__)