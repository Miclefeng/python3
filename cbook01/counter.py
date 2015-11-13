# counter.py
from collections import Counter
word = ['x','x','y','z','a','b','c','x','z','z','x','a','b']
word_counts = Counter(word)
top_three = word_counts.most_common(3)
print(top_three)
# [('x', 4), ('z', 3), ('b', 2)]

print(word_counts['x'])		# 4
# [('x', 4), ('z', 3), ('b', 2), ('a', 2), ('y', 1), ('c', 1)]

print(word_counts.most_common())	

word2 = ['x','y','z','a','c','b','c','a']
word_counts.update(word2)
print(word_counts.most_common())
# [('x', 5), ('a', 4), ('z', 4), ('b', 3), ('c', 3), ('y', 2)]

a = Counter(word)
b = Counter(word2)
print(sorted(zip(a.keys(),a.values())))
# [('a', 2), ('b', 2), ('c', 1), ('x', 4), ('y', 1), ('z', 3)]

print(sorted(zip(b.keys(),b.values())))
# [('a', 2), ('b', 1), ('c', 2), ('x', 1), ('y', 1), ('z', 1)]
print(a + b)
# Counter({'x': 5, 'a': 4, 'z': 4, 'c': 3, 'b': 3, 'y': 2})
print(a - b)
# Counter({'x': 3, 'z': 2, 'b': 1})


