# coding:utf-8
path = r'C:\Users\tianyf\Desktop\优化.txt'.decode('utf-8')
print path
f = open(path, 'r')
for line in f:
  print(line.decode('utf-8')),
  # 逗号表示不换行，在3.X中为print(str1, end="")
f.close()

# enmerate可以显示序号
f1 = open(path, 'r')
for i, line in enumerate(f1):
  print i, line.decode('utf-8'),
f1.close()