y = int(input())
i = 1
j = 1
for a in range(y):
    for b in range(y):
        x= j*i
        print(x,end=' ')
        i+=1
    j+=1
    i = 1
    print("")
    


