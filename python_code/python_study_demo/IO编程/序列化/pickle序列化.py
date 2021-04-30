import pickle

d = dict(name='Bob', age=20, score=88)
# pickle.dumps()方法把任意对象序列化成一个bytes，然后就可以把这个bytes写入文件

with open('test.txt', 'wb') as f:
    # pickle.dump()直接把对象序列化后写入一个file-like Object
    pickle.dump(d, f)

    