def createGenerator():
    ls = range(0, 4)
    for i in ls:
        yield i**2

generator = createGenerator()
print(generator)
for i in generator:
    print(i)
