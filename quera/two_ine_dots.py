a = input()
b = []
for i in a:
    b.append(i)

if int(b[0]) == int(b[4]):
    print('Vertical')
if int(b[2]) ==int(b[6]):
    print('Horizontal')
elif int(b[2]) !=int(b[6]) and int(b[0]) != int(b[4]):
    print('Try again')