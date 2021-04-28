class Student(object):
    pass

# 给实例绑定属性
s = Student()
s.name = 'Tom'
print(s.name)

# 给实例绑定方法
# 但对某一个实例绑定方法，对其他实例是不起作用的
def set_age(self, age):
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(20)
print(s.age)

# 为了给所有的实例都绑定方法，可以给class绑定方法
def set_score(self, score):
    self.score = score
Student.set_score = set_score  # 给Student类绑定方法
s2 = Student()
s2.set_score(29)
print(s2.score)

# 通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现

# slots
# 为了限制实例的属性，python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class增加属性
class Teacher(object):
    
    __slots__ = ('name', 'age')

teacher1 = Teacher()
teacher1.name = 'Lily'
teacher1.age = 40
print(teacher1.name, teacher1.age)
# teacher1.school = 'qinghua'    #报错，因为Teacher类只能绑定name和age属性

# 注意：使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class xiaozhang(Teacher):
    pass

xz = xiaozhang()
xz.name = 'bob'
xz.age = 89
xz.school = 'qinghua'
print(xz.name, xz.age, xz.school)   # xiaozhang类是Teacher的子类，但是他不受__slots__限制，可以任意绑定属性