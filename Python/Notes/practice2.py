# def opposite(a, b):
#     if a or b < 0:

#         print('False')
#     elif a and b > 0:
#         print ('True')
# UI = int(input('enter positive or negative integer: '))
# ui_two = int(input('enter positive or negative integer: '))

# opposite(a = UI, b = ui_two)


def opposite(a, b):
    if (a> 0 and b < 0):
        print('true')
    elif (a < 0 and b > 0):
        print('true')
    else:
        print('false')