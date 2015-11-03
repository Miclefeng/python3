# with.py 
num = 1
with open('story.txt','r') as f:
    for line in f:
        print('%04d %s' % (num,line), end = '')
        print('{0:04} {1}'.format(num,line),end = '')
        num = num + 1
