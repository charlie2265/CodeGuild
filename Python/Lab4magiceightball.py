# Charlie
# Lab4 magic eightball
import random
# print welcome screen
print('Welcome to the Magic Eightball program?')

# prompt user to ask a question
# input inside of loop
M_eight = ['It is certain', 'It is decidedly so', 'Without a doubt', 'yes']

while True:
    user = input('Please ask me a question! :')
    print(random.choice(M_eight))

    if user == 'done':
        print('Goodbye')
        break
   
# use the random module to simulate a magic eight ball answer



