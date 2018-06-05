# forrange.py 
result = []
# range() 的范围不包括右边界
for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result)

girls = ['alice','bernice','clarice']
boys = ['chris','arnold','bob']
print([b+'+'+g for b in boys for g in girls if b[0] == g[0]])

print()

result = []
for b in boys:
    for g in girls:
        if(b[0] == g[0]):
            result.append(b+'+'+g)
print(result)

letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0],[]).append(girl)
    print(letterGirls)
print([b+'+'+g for b in boys for g in letterGirls[b[0]]])
            