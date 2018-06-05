for i in range(10,0,-1) :
    print(i)
    
i = 0
while i < 10 :
    print(i)
    i = i + 1 # add 1 to i
    
n = int(input('Enter an integer >= 0: ').strip())
fact = 1
for i in range(2,n+1) :
    fact = fact * i
print(str(n)+' factorial is '+str(fact))

n = int(input('Enter an integer >= 0: ').strip())
fact = 1
i = 2
while i <= n :
    fact = fact * i
    i = i + 1
print(str(n)+' factorial is '+str(fact))