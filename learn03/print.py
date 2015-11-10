# print.py
import sys

def print3(*args,**kargs):
	sep = kargs.get('sep',' ')
	end = kargs.get('end','\n')
	file = kargs.get('file',sys.stdout)
	output = ''
	first = True
	for arg in args:
		output += ('' if first else sep) + str(arg)
		first = False
	file.write(output + end)

print3(1,2,3)

print3(1,2,3,sep='')
print3(1,2,3,sep='...')
print3(1,[2],(3,),sep='...')
print3(3,4,5,sep='',end='')
print3(1,2,3,sep='xxx',end='.......')
print3(6,7,8)
