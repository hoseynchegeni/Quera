from audioop import reverse


NumList = []
while True:
    number = int(input())
    if number == 0 :
        break 
    else:
        NumList.append(number)

NumList.reverse()
for i in NumList:
    print(i)