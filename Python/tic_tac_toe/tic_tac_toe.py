class Player:

    def __init__(self, name, token):
        self.name = name
        self.token = 'x', 'o'

    def __repr__(self):


        pass
        
class Board():

    def __init__(self):
        self.board = [['  ', '  ', '  '],
                      ['  ', '  ', '  '],
                      ['  ', '  ', '  ']]
        

    def __repr__(self):
        ''' Returns a pretty string representation of the game board'''
        board = ''
        for row in self.board:
            board += '|'.join(row)  + '\n'
        return f'{board}'
            
            
    def move(self,x, y, player):
        '''Place a player's token character string at a 
        given coordinate (top-left is 0, 0), x is horizontal position, y is vertical position.
        check if space is taken. 
        convert indexes. 
        '''
        x =  
        y = 
        



        
    def calc_winner(self):
        '''What token character string has won or None if no one has.'''
        pass
    
    def is_full(self):
        '''Returns true if the game board is full.'''
        pass

    def is_game_over(self):
        '''Returns true if the game board is full or a player has won.
        '''    
        pass


def main():
    board = Board()
    print(board)
    # print(board.move)

main()
    

        
    


    

    
    

    
