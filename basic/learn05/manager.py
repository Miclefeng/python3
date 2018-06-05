# manager.py

class Person:
	def __init__(self,name,job=None,pay=0):
		self.name = name
		self.job = job
		self.pay = pay
	def lastName(self):
		return self.name.split()[-1]
	def giveRaise(self,percent):
		self.pay = int(self.pay * (1 + percent))
	def __str__(self):
		return '[Person: %s, %s]' % (self.name,self.pay)

class Manager:
	def __init__(self,name,pay):
		self.person = Person(name,'mgr',pay)
	def giveRaise(self,percent,bonus=.10):
		self.person.giveRaise(percent + bonus)
	def __getattr__(self,attr):
		return getattr(self.person,attr)
	def __str__(self):
		return str(self.person)

if __name__ == '__main__':
	sue = Person('Sue Jones',job='dev',pay=100000)
	print(sue.lastName())		# Jones
	sue.giveRaise(.10)
	print(sue)					# [Person: Sue Jones, 110000]
	tom = Manager('Tom Jones',50000)
	print(tom.lastName())		# Jones
	tom.giveRaise(.10)
	print(tom)					# [Person: Tom Jones, 60000]





