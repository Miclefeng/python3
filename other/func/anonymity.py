
def add(x, y):
    return x + y
print(add(1, 2))

func = lambda x, y : x + y
print(func(1, 2))

# ?: 三元运算
func2 = lambda x, y : x if x > y else y
print(func2(2, 4))
