try:
    s = open('E:/work/2021HW/dcn_open.txt', 'r')
    for line in s.readlines():
        print(line.strip())
finally:
    if s:
        s.close()
    
# 等同于 上面的代码，不用再写close()
with open('E:/work/2021HW/dcn_open.txt', 'r') as t:
    print(t.read())

# 按字节读取 read(size)
# 每次读取一行内容 readline()
# 一次读取所有内容并按行返回list  readlines()

