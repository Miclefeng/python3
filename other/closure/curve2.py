
def f1():
    a = 10
    def f2():
        # a 被Python认为是一个局部变量，没有引用外部环境变量a，不是闭包
        a = 20
        print(a)
    print(a)
    f2()
    print(a)

f1()
