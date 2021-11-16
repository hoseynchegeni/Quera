import random
def game_night():
    round = 1
    user_score = 0
    os_score = 0 
    print('=====================')
    print('Alright, lets goooooo')
    print('=====================')
    while True:
        os_choice_option = ['R','S','P']
        number = random.randint(0,2)
        os_choice = os_choice_option[number]
        print(f'Round {round}   |||  {username}: {user_score} and AI: {os_score} ||| (R)ock, (S)cissor, (P)aper ')
        user_choice = input('>>>')
        if user_choice.upper() == os_choice:
            print('Its equal')
            round += 1
        elif user_choice.upper() == 'R' and os_choice == 'S':
            round += 1
            user_score += 1 
            if user_score == 3:
                break
            print('Rock beat Scissor')       
        elif user_choice.upper() == 'R' and os_choice == 'P':
            round += 1
            os_score += 1 
            if os_score == 3:
                break
            print('Paper beat Rock')
        elif user_choice.upper() == 'S' and os_choice == 'R':
            round += 1
            os_score += 1
            if os_score == 3:
                break 
            print('Rock beat Scissor')
        elif user_choice.upper() == 'S' and os_choice == 'P':
            round += 1
            user_score += 1 
            if user_score == 3:
                break
            print('Scissor beat Paper')
        elif user_choice.upper() == 'P' and os_choice == 'R':
            round += 1
            user_score += 1 
            if user_score == 3:
                break
            print('Paper beat Rock')
        elif user_choice.upper() == 'P' and os_choice == 'S':
            round += 1
            os_score += 1
            if os_score == 3:
                break
            print('Scissor beat Paper')
        else:
            print('Its not a valid choice, try again in next round')
    print (f'Final score | {username}: {user_score} and AI: {os_score}  ')
    print('======================================================')
    if user_score > os_score : 
        print('You Win')
        choice = input("If you want to try again enter 'y'or press any key to exit: ")
        if choice == 'y':
            game_night()
        else:
            exit()
    else:
        print('You Lose')
        choice = input("If you want to try again enter 'y'or press any key to exit: ")
        if choice == 'y':
            game_night()
        else:
            exit()


        
    
print('Hi, Welcome to Rock, Scissor, Paper game')
print('---------------------------------------')
username = input('Enter your name:  ')
print('=======================')
choice = input("If you are ready to play Enter 'y'or press any key to exit:  ")
if choice == 'y':
    game_night()
else:
    exit()