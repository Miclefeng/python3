#varargs.py
def tracer(func,*pargs,**kargs):
	print('calling:',func.__name__)
	print(pargs,kargs)
	return func(*pargs,**kargs)

def func(a,b,c,d):
	return a + b + c + d

print(tracer(func,1,2,3,d=4))
