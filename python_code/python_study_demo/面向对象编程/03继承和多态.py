class Animal(object):
    def run(self):
        print('Animal is running...')

# 继承：子类获得了父类的全部功能
class Dog(Animal):

    # 子类的run()覆盖了父类的run()
    def run(self):
        print("Dog is running..")

    def eat(self):
        print('Eating meat...')

class Cat(Animal):

    pass

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
    def wolf(self):
        print("wolf")

def run_twice(a):
    a.run()
    a.run()



dogge = Dog()

# 只要存在相同的方法，就可以调用run_twice()
run_twice(dogge)
run_twice(Tortoise())
# 因为Cat是Animal的子类，因此Cat自身虽然没有定义run方法，但是他继承了Animal的run方法，同样可以调用run_twice()
run_twice(Cat())

# # 判断变量是否是某个类型：isinstance()
# print(isinstance(dogge, int))  # False
# print(isinstance(dogge, Dog))  # True

# # 继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类
# print(isinstance(dogge, Animal))