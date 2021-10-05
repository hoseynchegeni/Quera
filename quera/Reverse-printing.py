y = []
zero_check = []
while True:
    x = input()
    if int(x) >=1000:
        break
    zero_check.clear()
    for i in x:
        zero_check.append(int(i))
    zero_check.reverse()
    if zero_check[0] == 0:
            break
    y.append(int(x))
    y.reverse()
    print(y)

    