from functools import reduce

# reduce 连续计算,连续调用lambda
list_x = ['1', '2', '3', '4', '5']
r = reduce(lambda x, y: x + y, list_x, 'ABC')
print(r)

def add(x, y):
    return (x[0] + y[0], x[1] + y[1])
list_y = [(0, 1), (2, 3), (-1, -2), (3, 4)]
s = reduce(add, list_y)
print(s)
