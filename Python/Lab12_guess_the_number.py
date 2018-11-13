# Charlie Lab 12 guess the number
# import random
import random


#to see the computer guess

i = 0
while i < 3:
    com_guess = random.randint(1, 10)
    user_guess = int(input('pick a number between 1 & 10 :'))
    print(com_guess)
    i += 1
    if user_guess == com_guess:
        break




        
    

    
