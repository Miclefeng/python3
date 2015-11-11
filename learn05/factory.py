# factory.py
def factory(aClass,*args):
	return aClass(*args)

class Spam:
	def doit(self,message):
		print(message)

class Person:
	def __init__(self,name,job):
		self.name = name
		self.job = job

object1 = factory(Spam)
object1.doit("code")
object2 = factory(Person,"Guido","guru")
print(object2.name,object2.job)