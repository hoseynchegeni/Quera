number = int(input())
index = 0
while index < number :
    name = input()
    index += 1 
NameList = []
for i in name:
    NameList.append(i)
NameList = list(dict.fromkeys(NameList))
print(len(NameList))