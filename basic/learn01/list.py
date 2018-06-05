# list.py 
import os
def list_cwd():
    return os.listdir(os.getcwd())
print(list_cwd())

def files_cwd():
    return [p for p in list_cwd() if os.path.isfile(p)]
print(files_cwd())
def folders_cwd():
    return [p for p in list_cwd() if os.path.isdir(p)]
print(folders_cwd())

def list_py(path = None):
    if path == None:
        path = os.getcwd()
    return [fname for fname in os.listdir(path) if os.path.isfile(fname) if fname.endswith('.py')]
print(list_py())

def size_in_bytes(fname):
    return os.stat(fname).st_size
def cwd_size_in_bytes():
    total = 0
    for name in files_cwd():
        total = total + size_in_bytes(name)
    return total
def cwd_size_in_bytes2():
    return sum(size_in_bytes(f) for f in files_cwd())

print(cwd_size_in_bytes())
print(cwd_size_in_bytes2())
