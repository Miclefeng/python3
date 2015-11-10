# maxs.py

def maxs(func,*args):
	res = args[0]
	for arg in args[1:]:
		if func(arg,res):
			res = arg
	return res

def lessthan(x,y): return x < y  #  取最小值

def bigthan(x,y): return x > y	 # 取最大值

print(maxs(lessthan,4,5,6,7,2,4,3,1))
print(maxs(bigthan,9,2,4,6,1,5,4))
