# Charlie
# Lab6 random emoticon
import random

eyes = [';', ':', '8', '?']
nose = ['3', '>', '^', 'c']
mouth = ['p', ')', ']', '|']

# while loop to do the "action" 5 times
i = 0
while i < 5:
    pick_eyes = random.choice(eyes) # action to pick from a list
    pick_nose = random.choice(nose)
    pick_mouth = random.choice(mouth)

    print(f'{pick_eyes}{pick_nose}{pick_mouth}') # f string to display the random choices
    i += 1
