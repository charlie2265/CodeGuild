#Charlie Lab 4 calculator
# 
# 
# 
# 
# 

nums = []

nums = []
while True:
    user = input('What function would you like to: ')  # prompt user

    if user == 'done':  # allow user to end program

        break  # end loop with done

    else:
        # define the users input
        FirstIn = int(input('enter your first number : '))
        SecondIn = int(input('enter second number: '))  # define users input

        if user == '+':
            # using if/elif statements perfom the users functions.
            print(FirstIn + SecondIn)
        elif user == '-':
            print(FirstIn - SecondIn)
        elif user == '*':
            print(FirstIn * SecondIn)
        elif user == '/':
            print(FirstIn / SecondIn)
