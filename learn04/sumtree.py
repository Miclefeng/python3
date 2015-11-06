# sumtree.py

def sumtree(l):
	tot = 0
	for x in l:
		if not isinstance(x,list):
			tot += x
		else:
			tot += sumtree(x)
	return tot

l = [1,[2,[3,4],5],6,[7,8]]
print(sumtree(l))

print(sumtree([1,[2,[3,[4,[5]]]]]))
print(sumtree([[[[[1],2],3],4],5]))

