from io import StringIO

# f = StringIO('Hello!\nHi!\nGoodbye!')

# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())
### >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 第一种方式
f = StringIO()
f.write('Hello\nworld\n!')
# 这里引入了 stream position的概念，当我们对StringIO流通过write写入内容时，指针指向了字符串的末尾
# 此时通过readline读取的内容从指针指向的位置开始，因此为空。我们可以通过tell方法看一下文件的当前位置
print(f.tell())   # 结果是13，即字符串的尾部
s = f.readline()  
print(s)          # 输出为空

# 若想输出成功，可以通过seed方法将指针指向字符串开头
f.seek(0)
s = f.readline()
print(s)

### >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 第二种方式
# 用一个str初始化StringIO
f = StringIO('Hello\nworld\n!')
# 这种方式，指针指向了开头，可以用tell方法测试一下
print(f.tell(),'\n')  # 输出0
# 此时可以通过readline直接输出
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())