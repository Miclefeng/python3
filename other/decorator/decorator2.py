import time

def decorator(func):
    # *args 可变参数
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)
    return wrapper

@decorator
def f3(func1, func2, **kw):
    # 关键字参数，形参和实参定义的名 不能一样
    print(kw)

@decorator
def f2(a, b):
    print("this is fun2 " + a + b)

@decorator
def f1(a):
    print("this is a func1 " + a)

# f = decorator(f1)
# f()
f1('func1')
f2('fun2','test')
f3("Test3", "Test", a=1, b=2, c='123')
