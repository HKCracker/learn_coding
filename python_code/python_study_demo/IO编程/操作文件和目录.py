import os

# 查看当前目录的绝对路径:
print(os.path.abspath('.'))

# 在当前路径下，想要新建一个testdir目录

# 拼接想要增加的目录名称，显示新目录的完整路径
print(os.path.join('d:\Coding\python_code\python_study_demo\IO编程', 'testdir'))
# 输出  d:\Coding\python_code\python_study_demo\IO编程\testdir

# 创建该目录
# 方式一：利用路径拼接返回一个想要创建的目录的完整路径，然后利用mkdir创建
os.mkdir(os.path.join('d:\Coding\python_code\python_study_demo\IO编程', 'testdir1'))
# 方式二：直接写上完整路径
os.mkdir(r'd:\Coding\python_code\python_study_demo\IO编程\testdir2')


# 删除该目录，也是两种方式类似于创建，只不过方法替换成了rmdir
os.rmdir(os.path.join('d:\Coding\python_code\python_study_demo\IO编程', 'testdir1'))
os.rmdir(r'd:\Coding\python_code\python_study_demo\IO编程\testdir2')