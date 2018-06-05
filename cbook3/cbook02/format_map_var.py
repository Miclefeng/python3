# format_map_var.py
s = "{name} has {n} message"
print(s.format(name='Guido',n=37))

name = "Guido"
n = 32
print(s.format_map(vars()))

class Info:
	def __init__(self,name,n):
		self.name = name
		self.n = n

a = Info("Guido",37)
print(s.format_map(vars(a)))

class safesub(dict):
	def __missing__(self,key):
		return '{' + key + '}'

del n
print(s.format_map(safesub(vars())))

import os 

print(os.get_terminal_size().columns)


