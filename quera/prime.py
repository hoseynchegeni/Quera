a = int(input())
b = int(input())
accumulator = 0
for i in range(a, b+1):
    for j in range(1, i+1):
        if i % j == 0 :
            accumulator += 1
    if accumulator == 2 :
        print(i)
        accumulator = 0 
    else:
        accumulator = 0     
