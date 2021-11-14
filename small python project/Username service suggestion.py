#Username service suggestion
import random

class person:
    def __init__(self,first,last,birthyear,username):
       self.first = first 
       self.last = last
       self.birthyear = birthyear
       self.username = username

person_1 = person
print("Welcome")
first = input('Enter your first name:')
person_1.first = first
last = input('Enter your last name:')
person_1.last = last
year = input('Enter your  birth year:')
person_1.birthyear = year
Suggested_username = []
create_username = (f'{first[0]}.{last}')
Suggested_username.append(create_username)
create_username =  (f'{first}{last}')
Suggested_username.append(create_username)
create_username = (f'{last}{year}')
Suggested_username.append(create_username)
number = random.randint(1000,9999)
create_username = (f'{first}{number}')
Suggested_username.append(create_username)
loop_counter = 1
for i in Suggested_username:
    print('---------')
    print(f'{loop_counter}: {i}')
    loop_counter+=1
username = input('Which username you want?')
print('Successfully registered')


