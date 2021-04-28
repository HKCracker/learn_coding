# g = (x * x for x in range(10))
# for n in g :
#     print(n)

# 斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


# 将斐波那契数列写成generator的形式
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

# 调用生成器时，需要先生成一个generator对象，然后利用next()不断获取值
f = fib(10)
for n in f:
    print(n)


# example : 杨辉三角
L=[1]

while True:

    try:

        yield L

        L=[L[i]+L[i+1] for i in range(len(L)-1)]

        L=[1]+L[:]+[1]

    except StopIteration as e:

        print('Generator return value:', e.value)

        break