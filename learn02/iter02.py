
l = [1,2,3]
for x in l:
	print(x ** 2, end=' ')

print('\n')
i = iter(l)
while True:
	try:
		x = next(i)
	except StopIteration:
		break
	print(x ** 2,end='   ')

