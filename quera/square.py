a = int(input())
b = a-2
c = ' '*b
for i in range(a):
    if i == 0:
        print('*'*a) 
    elif i == a-1:
        print('*'*a) 
    else:
        print(f'*{c}*')