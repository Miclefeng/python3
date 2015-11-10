# lambda.py
def func(x,y,z): return x + y + z
print(func(2,3,4))

f = lambda x,y,z:x + y + z
print(f(1,2,3))

x = (lambda a='fee',b='fie',c='foe':a + b + c)
print(x('wee'))

def knights():
	title = 'Sir'
	action = (lambda x:title + ' ' + x)
	return action

act = knights()
print(act('zss'))

