# Charlie Lab 4
# Display a letter grade from an integer input
import math
#  define a variable for user input
grade = int(input("What is your score?: "))
remainder = grade % 10

#  using if, elif, else print letter grade based on user input
if grade >= 90:
    letter = 'A' 
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade >= 60:
    letter = 'D'
else:
    letter = 'F'

if grade != 'F':
    remainder += '+'
    remainder += '-'

else:
    letter = 'F'
    

# if remainder > 5:
#     print('+') 
# elif remainder < 6:
#     print('-')
