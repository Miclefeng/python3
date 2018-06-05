# chainmap.py
from collections import ChainMap 

a = {'x':1,'z':3}
b = {'y':2,'z':4}
c = ChainMap(a,b)
print(c['x'],c['y'],c['z'])  	#  1 2 3
c['w'],c['z'] = 40,10
del c['x']
print(a)		#	{'w': 40, 'z': 10}

values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
print(values)
# ChainMap({'x': 3}, {'x': 2}, {'x': 1})
values = values.parents
print(values['x'])		# 2
values = values.parents
print(values['x'])		# 1
print(values)
# ChainMap({'x': 1})



