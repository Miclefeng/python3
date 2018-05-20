import time

def f1():
    print("this is func1")

def f2():
    print("this is func2")

def print_current_time(func):
    print(time.time())
    func()

print_current_time(f1)
print_current_time(f2)
