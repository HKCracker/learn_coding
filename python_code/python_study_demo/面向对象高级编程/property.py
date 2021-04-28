# Python内置的@property装饰器就是负责把一个方法变成属性调用的
class Student(object):
    def __init__(self, name):
        self._name = name
        
    @property
    def age(self):
        return self._name,self._age

    @age.setter   # 注意这里是age.setter
    def age(self, age):
        self._age = age

s1 = Student('Tom')
s1.age = 25
print(s1.age)