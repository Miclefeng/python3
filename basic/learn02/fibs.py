#fibs.py 
fibss = [0,1]
for i in range(8):
    fibss.append(fibss[-2]+fibss[-1])

print(fibss)

fibss = [0,1]
sum = input("How many Fibonacci do you want? ").strip()
for i in range(int(sum)-2):
    fibss.append(fibss[-2] + fibss[-1]) 
print(fibss)


