# word guessing game
import random 
def game_night():
    score = 0
    chance = 10
    counter = 1
    words_list = ['aa','bb','cc','dd','ee','ff','gg','hh','ii','jj','kk','ll','mm','nn','oo','pp','qq']
    print('-----------------------------')
    print('Alright, you have 10 chance to play if you answer 5 of 10 questions you win')
    print('-----------------------------')
    print('Alright, lets gooooooooooo')
    print('---------------')
    while chance > 0 :
        number = random.randint(0,len(words_list)-1)
        chosen_word= words_list[number]
        guess = input(f'{counter}-guess the word // start with {chosen_word[0]} and its {len(chosen_word)} word: ')
        if guess == chosen_word:
            score += 1
            print('Well done, its correct')
        else:
            print('Nope, try again')
        chance-=1
        counter+=1
    if score >= 5 :
         print(f'you win, your score is {score}')
    else:
        print(f'You lose, your score is {score}')
    choice = input("if you want t try again enter 'y' or press any key to exit")
    if choice == 'y':
        game_night()
    else:
        exit()
def start_game():
    print('Hi, Welcome to Word guessing game')
    print('----------------------------')
    username = input('Enter you name: ')
    print('---------------------------')
    start_game = input(f"alright {username}, if you want to play Word guessin Enter 'y' or press any key to exit")
    if start_game == 'y':
         game_night()
    else:
        exit()


start_game()
    
