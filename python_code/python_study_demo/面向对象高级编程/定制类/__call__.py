# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。

# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Tom')
s()

# 更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。

print(callable(s))
print(callable(Student('Tom')))
print(callable([1,2,3]))



# 重要实例
class Chain(object):
    def __init__(self, path=''):
       self.__path = path

    def __getattr__(self, path):
       return Chain('%s/%s' % (self.__path, path))  

    def __call__(self, path):
       return Chain('%s/%s' % (self.__path, path))

    def __str__(self):
       return self.__path

    __repr__ = __str__

print(Chain().users('michael').repos) # /users/michael/repos

'''
python 解释的时候从左往右计算，碰到. 就找前面计算得出的对象的属性，根据属性返回的结果得到一个新的对象；碰到()就将前面计算得出的对象当成一个函数，将括号里面的内容当成参数，传入到对象__call__函数中，根据返回的结果得到一个新的对象；一直这样解释下去
步骤拆解:
1. Chain()  这一步相当于创建了一个Chain实例，由于创建实例时并没有传入path属性值，因此此时self.__path的值为默认空''
2. Chain.users  这一步，相当于去查找Chain()实例中的users属性，由于没有该属性，故调用__getattr__方法，该方法返回一个新的实例Chain('/users')，在这个新的实例被创建时，__init__又重新触发，此时self.__path值为/users
3. 由于类Chain还实现了__call__方法，因此此时实例Chain('/users')时可被调用，可以看成是函数，括号内的michael相当于传入的参数，此时调用__call__方法，返回一个新的实例Chain('/users/Michael'),self.__path值为/users/Michael
4. .repos 这一步类似于步骤2，查找repos属性，没有就调用__getattr__方法，最终返回新的实例Chain('/users/Michael/repos')，此时self.__path值为/users/Michael/repos
5. print(Chain().users('michael').repos) 相当于打印实例Chain('/users/Michael/repos')，此时执行__str__方法，输出结果/users/michael/repos
'''