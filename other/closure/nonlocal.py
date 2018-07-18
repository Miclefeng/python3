origin = 0

def factory(pos):
    def go(step):
        # nonlocal 取消环境变量pos的局部变量属性
        nonlocal pos
        new_pos = pos + step
        # pos 内部环境变量，保存上次调用的状态，不能被内部重新定义、赋值
        pos = new_pos
        return new_pos
    return go

tourist = factory(origin)
print(tourist(2))
print(tourist.__closure__[0].cell_contents)
print(tourist(4))
print(tourist.__closure__[0].cell_contents)
print(tourist(6))
print(tourist.__closure__[0].cell_contents)
