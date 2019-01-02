from collections import namedtuple

Player = namedtuple('player', ['name', 'color'])

# class player:
#     def __init__(self):
#         self.name
#         self.color

class Game:
    def __init__(self):
        self.board = [['-' for x in range(7)]for y in range(6)]

    def __repr__(self):
        board = ''
        for row in self.board:
           board += '|'.join(row) + '\n'
        return board

    def get_height(self, position):
        '''return an int  of how many peices occupy a column. '''
        counter = 0
        for i in range(len(self.board)-1, -1, -1):
            row = self.board[i]
            print(row[position -1])
            find_token = row[position-1]
            if find_token == '-':
                break
            counter += 1
        return counter
        
    
    def move(self, player, position):
        x = position - 1
        y = 5 - self.get_height(position)
        print(y)
        if y < 0:
            raise ValueError('Error')
        self.board[y][x] = player.color

        
    
    def calc_winner(self):
        
        for y in range(len(self.board)-3):
            for x in range(len(self.board[y])-3):

                for i in range(4):
                #horizontal matches
                    if self.board[y+i][x] == self.board[y+i][x+1] == self.board[y+i][x+2] == self.board[y+i][x+3] and self.board[y+i][x] != '-':
                        return self.board[y+i][x]
                #vertical matches
                if self.board[y][x] == self.board[y][x+1] == self.board[y][x + 2] == self.board[y][x+3] and self.board[y][x] != '-':
                    return self.board[y][x]
                #diagonal matches
                if self.board[y+3][x] == self.board[y+2][x+1] == self.board[y +1][x+2] == self.board[y][x+3] and self.board[y][x+3] != '-':
                    return self.board[y][x + 3]
                if self.board[y][x] == self.board[y+1][x+1] == self.board[y+2][x+2] == self.board[y+3][x+3] and self.board[y][x] != '-':
                    return self.board[y][x]
        

                
        
    
    def is_full(self):
        for row in self.board:
            for cell in row:
                if cell == '-':
                    return False
        return True
        
    def is_game_over(self):
        return self.calc_winner() or self.is_full()
        
        

    
if __name__ == '__main__':
    game = Game()
    player1 = Player('1', 'y')
    player2 = Player('2', 'r')
    current_round = 1

    while not game.is_game_over():
        print(game)

        if current_round % 2 != 0:
            current_player = player1
        else:
            current_player = player2
        while True:
            move = input('Enter your move: ')
            try:
                position = int(move)
                if position < 1 or position > 7:
                    raise ValueError
                game.move(current_player,position)
                break
            except ValueError:
                print('Error')
        current_round += 1
print(game)
winner = game.calc_winner()
if winner:
    print(f'{winner} wins!')
else:
    print ('your all losers')

    

    

    
    
