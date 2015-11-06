# map01.py

counters = [1,2,3,4]
update = []
for x in counters:
	update.append(x+10)
print(update)

def inc(x): return x + 10

print(list(map(inc,counters)))

print(list(map((lambda x:x + 3),counters)))

def mymap(func,seq):
	res = []
	for x in seq: res.append(func(x))
	return res
print(list(map(inc,[1,2,3])))

print(mymap(inc,[1,2,3]))


print(list(map(pow,[1,2,3],[2,3,4]))) # 1**2 , 2**3 , 3**4
