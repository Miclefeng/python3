# dict_get.py 
people = {
        'Alice' : {
                'phone' : '2341',
                'addr'  : 'Foo drive 23'
                   },
        'Beth'  : {
                'phone' : '9102',
                'addr'  : 'Bar street 42'
                   },  
        'Cecil' : {
                'phone' : '3158',
                'addr'  : 'Baz avenue 90'
                   }
          }
labels = {'phone':'phone number','addr':'address'}

name = input('Name: ').strip()

request = input('Phone number(p) or address(a)?').strip()

key = request
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

person = people.get(name,{})
# get(key,key) 提供默认值
label = labels.get(key,key)
result = person.get(key,'not avaliable')
print("%s's %s is %s." % (name,label,result))