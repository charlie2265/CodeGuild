nums = [] #empty list.

while True: #while loop with the condition of true
    num = int(input('do something: ')) #input variable
    if num == 'done': #stops the loop
        break
    nums.append(int(nums)) #adds input data to nums list
print(nums) #prints nums list

# meyhods are functions atached to object
# conditionals always boil down to a boolean true or false
# while condition:
    # run code


# arr=[1,2,3]
# for i in range(len(arr)): #will 
# 
# #
# Create a for loop that prompts the user for a hobby 3 times, then appends each one to hobbies

hobbies = []

for i in range(3):  # range(3) make the loop happen 3 times.
    user = input(" what is your favorite hobby?")
    hobbies.append(user)  # the name of the list you wish to append goes first


def avg(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum / len(args)


nums = []
print('')

while True:
    user_input = input('enter').strip().lower()
    if user_input == 'done':
        break
    nums.append(int(user_input))
print(avg(*nums))
# lab23
with open(contacts.csv ,'r') as f:
    contents = f.read().split('\n')
csv = []
keys = [0]
keys = keys.split()
rows = [0]
print(csv)
print(keys)
print(rows)

for row in rows:
    row = row.split(',')
'''
a function returns some code 
'''
'''
recursion
