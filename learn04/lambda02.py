# lambda02.py
import sys
key = 'got'
d = {'already':(lambda:2 + 2),'got':(lambda:2 * 4),'one':(lambda:2 ** 6)}
print(d[key]())

# sys.stdout.write(str+'\n') = print()
showall = lambda x: list(map(sys.stdout.write,x))
t = showall(['spam\n','toast\n','eggs\n'])

show = lambda x:[sys.stdout.write(line+'\n') for line in x]
t = show(('bright','side','of','life'))
