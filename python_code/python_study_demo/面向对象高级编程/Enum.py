from enum import Enum, unique

# 除了通过继承 Enum 类的方法创建枚举类，还可以使用 Enum() 函数创建枚举类
# Enum() 函数可接受 2 个参数，第一个用于指定枚举类的类名，第二个参数用于指定枚举类中的多个成员
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 枚举类还提供了一个 __members__ 属性，该属性是一个包含枚举类中所有成员的字典，通过遍历该属性，也可以访问枚举类中的各个成员
for name, member in Month.__members__.items():
    # value属性则是自动赋给成员的int常量，默认从1开始计数
    print(name, '=>', member, ',', member.value)

# @unique装饰器可以帮助我们检查保证没有重复值
@unique
# 如果想将一个类定义为枚举类，只需要令其继承自 enum 模块中的 Enum 类即可
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday.Sun.value)
print(Weekday['Tue'])

class Color(Enum):
    # 为序列值指定value值
    red = 1
    green = 2
    blue = 3

#调用枚举成员的 3 种方式
print(Color.red)
print(Color['red'])
print(Color(1))
#调取枚举成员中的 value 和 name
print(Color.red.value)
print(Color.red.name)
#遍历枚举类中所有成员的 2 种方式
for color in Color:
    print(color)