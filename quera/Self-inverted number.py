number = input()
a = []
b = [] 
for i in number:
    a.append(i)
    b.append(i)
a.reverse()
if a == b:
    print('YES')
else:
    print('NO')