numbers = []
for i in range(4):
    x = int(input())
    numbers.append(x)
print(f'sum : {round(sum(numbers),5)}')
print(f'Average : {sum(numbers)/len(numbers)}')
print(f'Product : {numbers[0]*numbers[1]*numbers[2]*numbers[3]}')
print(f'MAX : {max(numbers)}')
print(f'MIN : {min(numbers)}')

