# person.py 
class Person:
    """ Class to represent a person """
    def __init__(self):
        self.name = ''
        self.age = 0
    def display(self):
        print("Person('{0}',{1})".format(self.name,self.age))
p = Person()
print(p)
print(p.age)
print(p.name)
p.age = 55
print(p.age)
p.name = 'Moe'
print(p.name)
p.display()

def __str__(self):
    return "Person('{0}',{1})".format(self.name,self.age)
print(__str__(p))
        