# lambda01.py
def func():
	x = 4
	action = (lambda n: x ** n)
	return action
x = func()
print(x(2))

def makeActions():
	acts = []
	for i in range(5):
		acts.append(lambda x,i = i: i ** x)
	return acts
acts = makeActions()
print(acts[0](2))
print(acts[4](2))
