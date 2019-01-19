#Charlie Lab 5 random emoticon

# create a password of a certain length.
import random
# user input as an int value
user_input = int(input('Choose a number length for your password?'))
# define string to pull charactors randomly to use in password
password = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
generate = ' ' #use an empty string variable this will keep the characters on one line

i = 0 #while loop to iterate through the password variable
#loop through user int value
while i <= user_input:
    generate += random.choice(password) # choosing characters and putting them in empty string
    i += 1

print(f'here is your {user_input} character password') # f string to repeat back user selection
print(generate) # display generated password
