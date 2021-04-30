from io import BytesIO

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())


ff = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(ff.read())