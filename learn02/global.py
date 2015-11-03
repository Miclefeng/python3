#global.py 
def try_to_change(n):
    global new
    new = n
    new = 'Mr.Gumby'

name = 'Mrs.Entity'
try_to_change(name)
print(new)
print(name)

# def store(data,full_name):
#     names = full_name.split()
#     if len(names) == 2: names.insert(1,'')
#     labels = 'first','middle','last'
#     for label,name in zip(labels,names):
        