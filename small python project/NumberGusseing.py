import random
def game_night():
    attempt = 3
    print('Alright lets goooooooo try your best')
    print('*************************')
    
    number = random.randint(1,20)
    while attempt > 0:
        print(f'you have {attempt} attempt to guess the number')
        choose = int(input('Guess the number:'))
        attempt -= 1
        if choose == number:
            print('well done its correct')
            print('--------------')
            play_again = input('Do you want to play again? y/n:  ')
            if play_again == 'y':
                game_night()
            else:
                print('ok thank you for play number guessing game bye bye')
                exit()
        elif choose > number:
            print('The correct nmberis lower')
            print('*************************')
        elif choose < number :
            print('Correct number is higher')
            print('*************************')
    print('ooooooh you dont have a chance th win the game')
    print('*************************')
    print(f'the correct number is {number}')
    print('*************************')
    play_again = input('oyou wanna play again? y/n: ')
    if play_again == 'y':
        game_night()
    else:
        print('ok thank you for play number guessing game bye bye') 



print('Hi, Welcome to the Numbergusseung game.')
print('---------------------------------------')
main_menu_choose = input('Do you want to play?  y/n: ')
if main_menu_choose == 'n':
    print('Ok Bye bye')
else:
    game_night()
