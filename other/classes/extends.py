
class Human():
    counter = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        print(self.name)
    def do_homework(self):
        print("Parent Homework")

# Human 是 Student 的父类, 且 Human 的声明必须在 Student 之前
class Student(Human):
    def __init__(self, school, name, age):
         self.school = school
         # 通过 Human 类调用 需要传递 self
         # Human.__init__(self, name, age)
         super(Student, self).__init__(name, age)

    def do_homework(self):
        super(Student, self).do_homework()
        print("English Homework")


student = Student('mount tai', 'micle', 26)
print(student.name)
print(student.age)
print(Student.counter)
student.get_name()
student.do_homework()
