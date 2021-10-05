a = input()
x = []
while True:
    for i in a:
       x.append(int(i))
    if len(x)>=2:
        a = str(sum(x))
        x.clear()
    else:
        print(a)
        break


    
