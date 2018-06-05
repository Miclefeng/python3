#password.py 
pwd = input('What is the password? ')
if pwd == 'apple' : #note use of == # instead of =
    print('Logging on ...')
else :
    print('Incorrect password.')
print('All done!') 

age = int(input('How old are you? '))
if age <= 2 :
    print('free')
elif 2 < age < 13 :
    print(' child fare')
else :
    print('adult fare')
    