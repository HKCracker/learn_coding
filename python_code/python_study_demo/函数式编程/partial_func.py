import functools

def test1(a, b, c, d=1):
    print(a+b+c+d)

test2 = functools.partial(test1, c=5)
test2(1,2)