class Student(object):
    # 类属性，归类所有，但类的所有实例都可以访问到-
    age = 1111
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

print(s.name, s.score, s.age)
s.age = 25 # 将实例s的age属性设置为25
print(s.age)
print(Student.age)
del s.age   # 删除了实例s的age属性后，又恢复为默认的类中的age属性值1111
print(s.age)