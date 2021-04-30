import os
# import shutil
# print(os.path.split(r'd:\Coding\python_code\python_study_demo\IO编程'))
# # 输出 ('d:\\Coding\\python_code\\python_study_demo', 'IO编程')

# print(os.path.splitext('d:\Coding\python_code\python_study_demo\IO编程\a.png'))

# 文件改名
#  os.rename('a.png', 'abc.png')

# 删除文件
# os.remove('a.png')

# shutil.copyfile('1.txt', '2.txt')

print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])