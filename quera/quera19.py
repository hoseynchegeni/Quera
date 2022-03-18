First = input() 
Second = input() 
if First[::-1] == Second[::-1]:
    print(f'{First} = {Second}')
elif First[::-1] > Second[::-1]:
    print(f'{Second} < {First}')
elif First[::-1] < Second[::-1]:
    print(f'{First} < {Second}')

