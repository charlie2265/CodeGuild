# Generate a list of 6 random numbers representing the winning tickets
# Start your balance at 0
# Loop 100, 000 times, for each loop:
# Generate a list of 6 random numbers representing the ticket
# Subtract 2 from your balance(you bought a ticket)
# Find how many numbers match
# Add to your balance the winnings from your matches
# After the loop, print the final balance
# #

import random
def pick6():
    winner_list = []
    for i in range(6):
        winner_list.append(random.randint(1,99))
    return winner_list


def num_matches(winning, ticket):
    matches = 0
    for i in range(len(ticket)):
        if winning[i] == ticket[i]:
            matches += 1
    return matches
        




def play100k():
    winning = pick6()
    balance = 0
    winnings = [0, 2, 7, 100, 50000, 1000000, 25,000000]
    # winnings = {}
    
    for i in range(100000):
        ticket = pick6()
        balance -= 2
        matches = num_matches(winning, ticket)
        payout = winnings[matches]
        balance += payout

        if matches > 2:   
            print(balance)
            print(winning)
            print(ticket)
            print(matches)
    print(payout)

def main():
    for i in range(100):
        play100k()
main()