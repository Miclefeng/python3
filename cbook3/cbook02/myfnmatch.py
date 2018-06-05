# fnmatch.py
from fnmatch import fnmatch,fnmatchcase
fnmatch('foo.txt','*.txt')
fnmatch('foo.txt','?oo.txt')

names = ['Dat1.csv','Dat2.csv','config.ini','foo.py']
print([name for name in names if fnmatch(name,'Dat*.csv')])
# ['Dat1.csv', 'Dat2.csv']

addresses = [
        '5412 N CLARK ST',
        '1060 W ADDISON ST',
        '1039 W GRANVILLE AVE',
        '2122 N CLARK ST',
        '4802 N BROADWAY',
    ]

print([addr for addr in addresses if fnmatchcase(addr,'* ST')])
# ['5412 N CLARK ST', '1060 W ADDISON ST', '2122 N CLARK ST']
print([addr for addr in addresses if fnmatchcase(addr,'54[0-9][0-9] *CLARK*')])
# ['5412 N CLARK ST']

