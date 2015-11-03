import sys
print('Welcome to Python!')

#print('jack ate ',' is dog',sep = '.')
#print('not fat')

name = input('What is your first name?').strip()
print('Hello '+name.capitalize()+'!')

age = input("How old are you today?").strip()
age10 = int(age)+10
print('In 10 years you will be '+str(age10)+' years old!')

ages = eval(input("? "))
print(ages)
