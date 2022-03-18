number = int(input())
Text_1 = input()
Text_2 = input()
indexer = 0 
test = 0 
while indexer < number:
    if Text_1[indexer] != Text_2[indexer]:
        test += 1
    indexer += 1 
print(test)