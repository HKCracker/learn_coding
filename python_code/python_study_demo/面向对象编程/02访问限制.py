# 防止外部对属性的修改，利用__变成私有变量
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    # 设置私有变量后，可以利用get方法 获取属性值
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
        
    # 特殊变量 __demo__  可以直接访问
    # _demo 这样的变量 外部是可以访问的，但是请视为私有变量处理
    


std = Student('tom', 23)
# 实际上，__name 已经被python解释器翻译成了_Student__name
print(std._Student__name)
# std.print_score()