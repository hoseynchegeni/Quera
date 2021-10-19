import random 
sin = {1:'sib',
       2:'samanu',
       3:'senjed',
       4:'somaghh',
       5:'sabze',
       6:'sir',
       7:'sonbol',
}
a = int(input())
check_unique = []
while len(check_unique) < a:
    b = random.randint(1,7)
    if b not in  check_unique:
        check_unique.append(b)
for i in range(len(check_unique)):
    print(sin[check_unique[i]])


