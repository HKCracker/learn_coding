# map()接受两个参数，一个是函数，一个是iterable map，将传入的函数一次作用于序列的每一个元素，并把结果作为新的iterator返回
def f(x):
    return x * x
r = map(f , [1,2,3,4,5])

print(list(r))

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce
def fn(x, y):
    return 10 * x + y
def char2int(x):
    return int(x)

print(reduce(fn,list(map(char2int,['1','3','5','7','9']))))
