a  = input()
b = []
for i in a.split():
    b.append(int(i))

if b[0] == 0 or b[1] == 0 or b[2] == 0 :
    print('No')
elif sum(b) == 180:
    print('Yes')
else:
    print('No')