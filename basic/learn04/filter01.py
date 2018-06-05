# filter01.py

print(list(filter((lambda x:x > 0),range(-5,5))))

res = []
for x in range(-5,5):
	if x > 0:
		res.append(x)
print(res)
