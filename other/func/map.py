list_x = [1, 2, 3, 4, 5, 6]

def square(x):
    return x**2

for x in list_x:
    square(x)

r = map(square, list_x)
print(list(r))

q = map(lambda x: x * x, list_x)
# 返回map对象，转换为list
print(list(q))


list_y = [1, 2, 3 ,4 ,5 ,6, 7, 8]
#lambda 以参数中元素最少的进行返回
s = map(lambda x, y: x**2 + y, list_x, list_y)
print(list(s))
