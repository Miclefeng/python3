# numnote.py 
def numnote(lst):
    msg = []
    for num in lst :
        if num < 0:
            s = str(num) + ' is negative'
        elif 0 <= num <=9:
            s = str(num)+ ' is a digit'
        else :
            return msg
        msg.append(s)
    return msg
print(numnote([1,5,-3,22]))

for msg in numnote([1,5,-6,22]): print(msg)
print('\n'.join(numnote([1,5,-6,22])))
lst = []
lst.extend('cat')
print(lst)
lst.extend([1,5,-3])
print(lst)
lst = ['a','b','c','d']
lst.pop(2)
print(lst)
lst.pop()
print(lst)
lst = ['a','b','c','a']
lst.remove('a')
print(lst)
lst = ['a','b','c','d']
lst.reverse()
print(lst)

print([n*n for n in range(1,11)])

result = []
for n in range(1,11):
    result.append(n*n)
print(result)
