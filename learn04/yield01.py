# yield01.py

def squares(n):
	for i in range(n):
		yield i ** 2

for i in squares(5):
	print(i,end=' <-> ')

print('\n')

def gen():
	for i in range(10):
		x = yield i
		print(x)

g = gen()
print(next(g))
print(g.send(1))
print(g.send(2))
print(next(g))
print(next(g))
print(next(g))

for num in (x ** 2 for x in range(4)):
	print('%s , %s' % (num,num/2))

l = (x ** 2 for x in range(4))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
