# Charlie Lab 12 guess the number
# import random
import random

n_guesses = []

while True:
    try:
        com_guess = random.randint(1, 10)
        user_guess = input('pick a number between 1 & 10 press done when you give up: ')
        user_guess = int(user_guess)
        n_guesses.append(user_guess)
        print(f'The computer chose {com_guess}.')
        

        if user_guess > com_guess:
            print('too high')
            
        elif user_guess <com_guess:
            print('too low')

    except ValueError:

        if user_guess == 'done':
            break
    if user_guess == com_guess:
             print('correct! type done to exit.')
             break
    
guesse = len(n_guesses)-1 + 1
print(f'Nice try it took you {guesse} tries')
