# kwonly.py
def f(a,*b,c=6,**d):
	print(a,b,c,d)
f(1,2,3,x=4,y=5)
f(1,2,3,x=4,y=5,c=3)
f(1,2,3,c=3,y=4)

# not keyword-only
def f(a,c=6,*b,**d): print(a,b,c,d)
f(1,2,3,x=4)


