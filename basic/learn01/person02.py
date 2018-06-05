# person02.py 
class Person:
    def __init__(self):
        self.name = 'HLK'
        self.age = 23
    def display(self):
        print(self)
    def __str__(self):
        return "Person('{0}',{1})".format(self.name,self.age)
    def __repr__(self):
        return str(self)
p = Person()
print(p)
print(str(p))