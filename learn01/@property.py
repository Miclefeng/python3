# person.py 
class Person:
    def __init__(self,name = '',age = 0):
        self._name = name
        self._age = age
    @property
    def age(self):
        return self._age
#     def set_age(self,age):
#         if 0 < age <= 150:
#             self._age = age
    @age.setter 
    def age(self,age):
        if 0 < age <= 150:
            self._age = age
    def dispaly(self):
        print(self)
    def __str__(self):
        return "Person('{0}',{1})".format(self._name,self._age)
    def __repr__(self):
        return str(self)
p = Person('Lia',33)
print(p)
p.age = 55
p.age = -4
print(p)