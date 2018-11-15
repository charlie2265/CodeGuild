# Charlie lab 17 palindrome and anagram
# Write a function check_palindrome which takes a string, and returns True if the string's a palindrome, or False if it's not.
#input a string
# copy to an empty string
# reverse empyt str
# compare input to empty str


def check_palindrome(pal):
    reversed_str = pal[::-1] # reverse UI
    
    if reversed_str == pal:
        return True
            
    return False
         
UI = input('enter a word: ')
print(check_palindrome(pal = UI)) # print to show what your function is doing.


# Convert each word to lower case(lower)
# Remove all the spaces from each word(replace)
# Sort the letters of each word(sorted)
# Check if the two are equal

def check_anagram(xx):
    xx = xx.lower()
    xx = xx.replace('','')
    xx = sorted(xx)
    print(xx) # visual to see the function performed twice
    return xx


first_word = input('enter first word: ')
second_word = input('enter second word: ')

if check_anagram(first_word) == check_anagram(second_word):
    print ('you got it!')
else:
    print('nope!')



            





        
        


     
           



    






