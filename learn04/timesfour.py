# timesfour.py
g = (c * 4 for c in 'SPAM')
print(list(g))

def timesfour(s):
	for c in s:
		yield c * 4
l = timesfour('spam')
print(list(l))

g = (c * 4 for c in 'SPAM')
i = iter(g)
print(next(i))
print(next(i))
print(next(i))
print(next(i))

G = timesfour('spam')
li = iter(G)
print(next(li))
print(next(li))
print(next(li))
print(next(li))
