# # 读文件
# file_obj = open('1.txt', mode='r', encoding='utf-8')
# data1 = file_obj.read()
# file_obj.close()
# print(data1)
# # 读图片
# file_obj2 = open('a.png', mode='rb')
# data2 = file_obj2.read()
# file_obj2.close()
# print(data2)

# # 将2进制转成文本格式
# text = data1.decode('utf-8')
# print(text)

# with open('a.png', 'rb') as f:
#     s = f.readlines()
#     for l in s:
#         print(l.strip())

# with open('1.txt','r') as f:
#     s = f.readlines()
#     for l in s:
#         print(l.strip())
    
with open('1.txt', 'w', encoding='utf-8') as f:
    f.write('123Hl算法12343534534534535')`
with open('1.txt','r',encoding='utf-8') as t:
    print(t.read())


