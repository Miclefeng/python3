# reduce01.py

from functools import reduce
print(reduce((lambda x,y:x + y),[1,2,3,4])) # 10

print(reduce((lambda x,y:x * y),[1,2,3,4])) # 24


def myreduce(func,seq):
	tally = seq[0]
	for next in seq[1:]:
		tally = func(tally,next)
	return tally

print(myreduce((lambda x,y:x + y),[1,2,3,4,5]))

print(myreduce((lambda x,y:x * y),[1,2,3,4,5]))
