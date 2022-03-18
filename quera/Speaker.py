name = input()
SplitName = []
for i in name:
    SplitName.append(i)
indexer = 1
print(''.join(SplitName))
while indexer < len(SplitName):
    SecondLoop = indexer
    for i in range(SecondLoop):
        SplitName[SecondLoop-1] = SplitName[SecondLoop]
        SecondLoop -= 1
    print(''.join(SplitName))
    indexer += 1 
        
