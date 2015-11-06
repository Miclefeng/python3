# mysum.py

def mysum1(l):
	return 0 if not l else l[0] + mysum1(l[1:])

def mysum2(l):
	return l[0] if len(l) == 1 else l[0] + mysum2(l[1:])

def mysum3(l):
	first,*rest = l
	return first if not rest else first + mysum3(l[1:])

print(mysum1([1,2,3,4]))
print(mysum2([1,2,3,4]))
print(mysum3([1,2,3,4]))


def mysum(l):
	if not l: return 0
	return nonempty(l)

def nonempty(l):
	return l[0] + mysum(l[1:])

print(mysum([1.1,1.2,3.3,4.4]))
