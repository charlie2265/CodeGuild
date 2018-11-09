# Charlie Lab8_make_change
# 
#convert dollar amount to number of coins
# in put is total amount
# output is number of quarters, dimes, nickles, and pennies
# For this, you'll have to use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

# enter a decimal(float) number
Money = input(" Enter your amount of money : ")
Money = int(float(Money) * 100)  # amount as an interger

# that amount is divided by 25 to make amount of quarters
Quarters = int(Money // 25)
Leftover = Money - (Quarters * 25)  # leftover from quarters

Dimes = int(Leftover // 10)  # leftover from quarters becomes dimes
Leftover = Leftover - (Dimes * 10)  # leftover from dimes

Nickels = int(Leftover // 5)  # leftover from dimes becomes nickels
Leftover = Money - Nickels * 5  # leftover from nickels

# needs to make leftover pennies.
Pennies = int(Leftover % 1)
Leftover = Money - Pennies * 1


print(
    f' you have {Quarters} quarters,  {Dimes} dimes, {Nickels} nickels, and {Pennies} pennies')

