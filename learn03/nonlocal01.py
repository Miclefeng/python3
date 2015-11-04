# nonlocal01.py
def tester(start):
	state = start
	def nested(label):
		print(label,state)
	return nested
f = tester(0)
f('spam')
f('ham')
print('\n')

def tester(start):
	state = start
	def nested(label):
		nonlocal state
		print(label,state)
		state += 1
	return nested
t = tester(0)
t('one')
t('two')
t('three')

class Test:
	def __init__(self,start):
		self.state = start
	def __call__(self,label):
		print(label,self.state)
		self.state += 1
h = Test(99)
h('juice')
h('pancakes')
