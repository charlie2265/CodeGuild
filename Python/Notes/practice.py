def latest_let(string):
    last = string[0]
    for char in string:
        if char.isalpha():
            if char > last:
                last =char
    if last.isalpha():
        return last
    return ''


print(latest_let('pneumonoultramicroscopicsilicovolcanoconiosis'))

# max number in a list

def max(nums):
    running_max = float('-inf')
    for num in nums:
        if num > running_max:
            running_max = num
    return running_max

print(max([2,4,-9000,7,11,0]))

def sum(sums):
    total = 0
    for num in sums:
        total += num
    return total

    # error handling

board = [ [1,2,3],
          [4,5,6],
          [7,8,9] ]
while True:

    try:
        position= int(input('enter a position: '))
        position = int(position)
        if position < 1 or position > 9:
            raise ValueError
        print('moved to position ' + position)
        break
    except ValueError as e:
        print('Enter a numer between 1 and 9')
        print(e)
ones = {1: 'one'}
tens = {2: 'twenty', 3: 'thirty'}
