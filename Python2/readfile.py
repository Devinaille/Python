# coding:utf-8
path = r'C:\Users\tianyf\Desktop\优化.txt'.decode('utf-8')
print path
f = open(path, 'r')
for line in f:
  print(line.decode('utf-8'))
f.close()