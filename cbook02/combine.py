# combine.py

def sample():
	yield "Is"
	yield "Chicago"
	yield "Not"
	yield "Chicago?"

text = ' '.join(sample())
print(text)

for part in sample():
	print(part,end=" ")