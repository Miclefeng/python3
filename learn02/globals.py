# globals.py 
def combine(parameter):
    print(parameter+globals()['parameter'])

parameter = 'berry'
combine('Shrub')

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
num = input("Enter the number? ").strip()
print(factorial(int(num)))