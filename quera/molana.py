from itertools import count
import re

WordList = []
Count = []
for i in range(5):
    word = input()
    WordList.append(word)
index = 0 
for i in WordList:
    index += 1 
    MolanaResualt = re.findall(r'(MOLANA)',i)
    HafezResualt = re.findall(r'(HAFEZ)',i)
    if MolanaResualt:
        Count.append(index)
    elif HafezResualt:
        Count.append(index)       
if len(Count) == 0:
    print('NOT FOUND!')
else:
    print(*Count, sep=" ")
