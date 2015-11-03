# write.py 
def make_story1():
    f = open('story.txt','w')
    f.write('Mary had a little lamb,\n')
    f.write('and the she had some more.\n')
make_story1()

def read_story(fname):
    print(open(fname,'r').read())
read_story('story.txt')
    
    