Sides = []
for i in range(3):
    number = int(input())
    Sides.append(number)
Sides.sort()
if (Sides[2]*Sides[2]) == (Sides[0]*Sides[0]) + (Sides[1]*Sides[1]) :
    print('YES')
else:
    print('NO')