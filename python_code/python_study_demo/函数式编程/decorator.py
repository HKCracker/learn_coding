import time

def timer(func):
    def wrapper(*args, **kw):
        start = time.time()
        func()
        end = time.time()
        print("used time = ", end - start)
    return wrapper

@timer
def step1():
    print('step1 begin ...')

step1()
