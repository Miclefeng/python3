# donesum.py
total = 0
s = input('Enter a number (or "done"): ').strip()
while s != 'done':
    num = int(s)
    total = total + num
    s = input('Enter a number (or "done"): ')
print('The sum is ' + str(total))

# donesumbreak.py
total = 0
while True:
    s = input('Enter a number (or "done"): ').strip()
    if s == 'done':
        break  # jump out of the loop
    num = int(s)
    total = total + num
print('The sum is ' + str(total))
