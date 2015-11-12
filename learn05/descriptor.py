# decriptor.py

class Descriptor(object):
	def __get__(self,instance,owner):
		print(self,instance,owner,sep='\n')

class Subject:
	attr = Descriptor()

x = Subject()
x.attr
print('-' * 20)
Subject.attr
