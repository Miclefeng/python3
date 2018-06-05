# startswith.py
filename = 'spam.txt'
filename.endswith('.txt')
filename.startswith('spam')

import os 
filenames = os.listdir('.')
print(filenames)
[name for name in filenames if name.endswith(('.c','.h'))]

any(name.endswith('.py') for name in filenames)

from urllib.request import urlopen

def read_data(name):
	if name.startswith(('http:','https:','ftp:')):
		return urlopen(name).read()
	else:
		with open(name) as f:
			return f.read()
choices = ['http:','ftp:']
url = 'http://www.python.org'
url.startswith(tuple(choices))