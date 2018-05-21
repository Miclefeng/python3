
# 列表推导式
a = [1, 2, 3, 4, 5, 6, 7]
b = [i*i for i in a]
c = [i**2 for i in a if i >= 5]
print(b)
print(c)

# 集合推导式
# set dict 都可以推导
d = {1, 2 ,3 ,4 ,5 ,6, 7}
e = {i**2 for i in a if i >=2}
print(e)
