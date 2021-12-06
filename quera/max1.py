all_numbers = []

first_num  = input()
second_num = input()

all_numbers.append(int(first_num))
for i in second_num.split():
    all_numbers.append(int(i))

print(max(all_numbers))