# Person.py 
__metaclass__ = type # 确定使用新式类

class Person:
    def setName(self,name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def greet(self):
        print("Hello world! I`m %s." % self.name)
        
foo = Person()
bar = Person()
foo.setName('Luke Skywalker')
foo.greet()
bar.setName('Anakin Skywalker')
bar.greet()
print(foo.name)
print(bar.name)
bar.name = 'Yoda'
bar.greet()