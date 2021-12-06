import math
x= []
number = input()
x= number.split()
for i in range(int(x[1])):
    y = int(x[0])/2
    x[0] = round(y)
print(math.ceil(x[0]))