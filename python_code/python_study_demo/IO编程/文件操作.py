import os
from io import StringIO

str1 = os.environ.get('PATH').replace(';', '\n')

s = StringIO(str1)

while True:
    m = s.readline()
    if m == '':
        break
    print(m.strip())

print(os.environ.get('Path'))