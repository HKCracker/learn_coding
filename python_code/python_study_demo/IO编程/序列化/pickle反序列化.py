import pickle

# pickle.loads方法
with open('test.txt','rb') as f:
    # 反序列化
    print(pickle.loads(f.read()))

# pickle.load方法
with open('test.txt','rb') as t:
    # pickle.load方法接受一个文件，从一个file-like Object中直接反序列化出对象
    s = pickle.load(t)
    print(s)