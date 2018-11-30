'''Charlie Lab 19 Blackjack 
First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)
figure out the point value of each card individually.
Number cards are worth their number, all face cards are worth 10.
Aces worth 1.
'''

def blackjack(x, y, z):

    '''set conditional for cards
    figure out the point value of each card individually.
    '''
    pass  
    
cards = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10 }       
   
def main():
    '''repl
    '''
    first_card = (input('whats your first card? : '))
    second_card = (input('whats your second card? : '))
    third_card =  (input('whats your third card? : '))
    first_card = cards[first_card]
    second_card = cards[second_card]
    third_card = cards[third_card]
        # print(blackjack(first_card, second_card, third_card))

    while True:
        i = first_card + second_card + third_card
        
        if i > 21:
           print (f'your score is {i} you busted')
        
        elif i == 21:
           print (f'your score is {i} BLACKJACK!')
        if i >= 15:
            return f'your score is {i} you should hit'
        
        break

    
    
main()
    
    
        
        

    
            
    
   
    

        
        
        
