# myzip.py
def myzip(*seqs):
	print(seqs) #('abc', 'xyz123')
	seqs = [list(s) for s in seqs]
	print(seqs)
	while all(seqs):
		yield tuple(s.pop(0) for s in seqs)

def mymapPad(*seqs,pad=None):
	seqs = [list(s) for s in seqs]
	while any(seqs):
		yield tuple(s.pop(0) if s else pad for s in seqs)

s1,s2 = 'abc','xyz123'

print(list(myzip(s1,s2)))
#[('a', 'x'), ('b', 'y'), ('c', 'z')]
print(list(mymapPad(s1,s2)))
#[('a', 'x'), ('b', 'y'), ('c', 'z'), (None, '1'), (None, '2'), (None, '3')]
print(list(mymapPad(s1,s2,pad=666)))
#[('a', 'x'), ('b', 'y'), ('c', 'z'), (666, '1'), (666, '2'), (666, '3')]


	
	
