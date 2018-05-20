list_x = [1, 0, 2, 0, 1, 0]

# 根据表达式返回值的 true , false 来过滤list_x中元素的值
r = filter(lambda x: True if x > 0 else False, list_x)
#r = filter(lambda x: x, list_x)
print(list(r))
