
class Student():
    # 定义类变量
    name = 'micle'
    age = 10
    sum1 = 0;

    # 构造函数,初始化对象的属性,只能返回None
    def __init__(self, name, age):
        # 定义实例化的变量
        self.name = name
        self.age = age
        self.__score = 0

        # 访问类的属性
        # self.__class__.sum1 += 1
        # print("当前班级学生总数：" + str(self.__class__.sum1))
        print(Student.sum1)
        return None
    def marking(self, score):
        if score < 0:
            return '不能打负分'
        self.__score = score
        print(self.name + '同学的本次考试分数为：' + str(self.__score))

    # 装饰器，让方法成为类方法，与 PHP 静态方法类似
    @classmethod
    def plus_sum(cls):
        cls.sum1 += 1
        print("当前班级学生的总数：" + str(cls.sum1))

    # 装饰器，让方法成为静态方法
    @staticmethod
    def add(x, y):
        print(Student.sum1)
        z = x + y
        print("This is a static method " + str(z))

    def do_homework(self):
        print("Homework!")


class Printer():

    def print_file(self):
        print('name : ' + name)
        print('age : ' + str(age))

student = Student('miclefengzss', 26)
Student.plus_sum()
student2 = Student('miclefeng2', 27)
Student.plus_sum()
student3 = Student('miclefeng3', 28)
Student.plus_sum()

Student.add(1, 2)
Student.add(2, 3)

# student.__init__()
print(student.name, student.age)
print(Student.name, Student.age)
print("\n")
print(student.__dict__)
print(Student.__dict__)
student.do_homework()

student.marking(66)
# 外部为实例设置变量
student.__score = 20
print(student.__score)
print(student.__dict__)
# student2未设置__score，调用内部私有变量报错
# print(student2.__score)
print(student2.__dict__)
# 读取内部私有变量
print(student2._Student__score)

# printer = Printer()
# printer.print_file()
