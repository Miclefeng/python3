# insert_title.py 
def insert_title(title,fname = 'story.txt'):
    f = open(fname,'r+')
    temp = f.read()
    temp = title  + '\n\n' + temp
    f.seek(0) # 让文件指针指向文件开头
    f.write(temp)
    print(open(fname,'r').read())
insert_title('Django')