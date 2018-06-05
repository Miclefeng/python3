# printfile.py 
def print_file1(fname):
    f = open(fname,'r')
    for line in f :
        print(line,end = '')
    f.close() # 这行代码是可选的
#print_file1('donesum.py')

def print_file2(fname):
    f = open(fname,'r')
    print(f.read())
    f.close()
    
def print_file3(fname):
    print(open(fname,'r').read())

    
print_file3('donesum.py')