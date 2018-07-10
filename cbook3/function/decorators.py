from time import ctime, sleep


def tsfunc(func):
    def wrappedFunc():
        print('[{:s}] {:s}() called'.format(ctime(), func.__name__))
        return func()
    return wrappedFunc


@tsfunc
def foo():
    pass

foo()
sleep(2)

for i in range(2):
    sleep(2)
    foo()