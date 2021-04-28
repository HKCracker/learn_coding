import types
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):

    def run(self):
        print("Dog is running..")

    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    pass

class Monkey(Dog):
    pass

def Fn():
    pass


# type
# 利用type判断类型，如果是函数类型,可以利用types包的方法进行判断
# 1.普通函数判断
print(type(Fn) == types.FunctionType)
# 2.内置函数判断
print(type(abs) == types.BuiltinFunctionType)
# 3.匿名函数判断
print(type(lambda x : x) == types.LambdaType)
# 4.产生器判断
print(type((x for x in range(10))) == types.GeneratorType)


# isinstance
# 对于class类型，使用type就很不方便，此时使用isinstance()
# isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上
d = Dog()
c = Cat()
a = Animal()
m = Monkey()
print(isinstance(d, Animal), 1)
print(isinstance(m, Animal), 2)
# 利用isinstance判断是否是某些类型中的一种
print(isinstance([1,2,3],(list, int, tuple)),3)
print(isinstance((1,2,3),(list, int, tuple)),4)



# dir
# dir()获取一个对象的所有属性和方法，返回一个包含字符串的list
print(dir('ABC'))

# 以下两种方法等价,因为如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法
print(len('ABC'))
print('ABC'.__len__())
# 如果我们自己写的类也想调用len方法，需要定义__len__方法
class Moon(object):
    def __len__(self):
        return 100
moon = Moon()
print(len(moon))


# 操作对象 getattr()、 setattr()、 hasattr()
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()
print(hasattr(obj, 'x'))   # 判断某一对象是否有属性 x
setattr(obj, 'y', 100)   # 设置一个属性 y
print(getattr(obj, 'y'))  # 获取属性 y

# 同样也可以判断方法
print(hasattr(obj, 'power'))
power = getattr(obj, 'power')
print(power())