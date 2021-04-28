# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义Student类
# 只有在没有找到属性的情况下，才调用__getattr__
class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

s = Student()
print(s.name)
print(s.score)
print(s.age())

# __getattr__默认返回就是None
print(s.aaaa)