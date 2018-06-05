# multidict.py

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(dict(d))
# {'a': [1, 2], 'b': [4]}
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(dict(d))
# {'a': {1, 2}, 'b': {4}}
d = {}
d.setdefault('a',[]).append(1)
d.setdefault('a',[]).append(2)
d.setdefault('b',[]).append(4)
print(dict(d))
# {'a': [1, 2], 'b': [4]}

pairs = {'a': 1, 'b': 4}
d = {}
# for k,v in pairs.items():
for k in pairs:
	if k not in d:
		d[k] = []
	d[k].append(pairs[k])

print(d)
# {'b': [4], 'a': [1]}

d = defaultdict(list)
for k in pairs:
	d[k].append(pairs[k])
print(dict(d))
# {'b': [4], 'a': [1]}




