s = 'spam'
offset = 0
for item in s:
	print(item,'apperars at offset',offset)
	offset += 1

for(offset,item) in enumerate(s):
	print(item,'appears at offset',offset)

print([c * i for(i,c) in enumerate(s)])
