# password2.py 
def main():
    pwd = input('What is the password? ').strip()
    if pwd == 'apple':
        print('Logging on ... ')
    else :
        print('Incorrect password.')
    print('All done!')
main()

def add(a,b):
    return a + b
x,y = 3,4
print(add(x,y))