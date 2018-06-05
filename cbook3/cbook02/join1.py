# join1.py
def sample():
	yield 'Is'
	yield 'Chicago'
	yield 'Not'
	yield 'Chicago?'

def combine(source,maxsize):
	parts = []
	size = 0
	for part in source:
		parts.append(part)
		size += len(part)
		if size > maxsize:
			yield ''.join(parts)
			parts = []
			size = 0
	yield ''.join(parts)

f = open('spam.txt','a')
for part in combine(sample(),32768):
	f.write(part+'\n')