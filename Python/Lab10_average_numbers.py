# Charlie Lab 10 average numbers


nums = []
#while loop to keep prompting the user.
while True:
    user = input('enter a number: ')  # prompt
    if user == 'done':  # allow user to end program
        break  # end loop with done
    else:
        nums.append(float(user))  # continue loop with user input

amount = 0
for i in nums:
                        # for loop to define amount variable and divide by what the user will put in.
    amount += i
    # amount = amount + amount (anything that will go in the empty list nums)
# now divide amount by the number of positions in the empty list nums
total = amount / len(nums)

print(str(total))  # total will be the average.


#
