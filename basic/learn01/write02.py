#write02.py 
import os
def make_story():
    if os.path.isfile('story.txt'):
        print('story.txt already exists')
    else:
        f = open('story.txt','w')
        f.write('Mary had a little lamb,\n')
        f.write('and then she had some more.\n')
make_story()