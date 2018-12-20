from Deck import Deck

class Hand:
    def __init__(self, card1, card2, name):
        self.cards = [card1, card2]
        self.name = name
        self.game_over = False
    
    def __repr__(self):
        return str(self.cards)


    def add(self, card):
        self.cards.append(card)

    def score(self):
        points = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                  '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
        total = 0

        for card in self.cards:
            total += points[card.rank]
        return total
class Dealer(Hand):
    def __init__(self, card1, card2,):
        super(). __init__(card1,card2, name='dealer')

    def __repr__(self):
        hidden_card = 'Hidden Card'
        cards = [hidden_card] + self.cards[1:]
        return str(cards)


    def visible_score(self):
        points = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
              '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
        total = 0
        cards = self.cards[1:]
        for card in cards:
            total += points[card.rank]
        return total

    def reveal_cards(self):
        print(self.cards)

class Game:
    def __init__(self, num_players = 1):
        self.deck = Deck()  # create deck
        self.deck.shuffle() # shuffle deck
        self.deck.cut()     # cut deck
        self.players = []
        self.dealer = Dealer(self.deck.draw(), self.deck.draw())
        for i in range(num_players):
            name = input(f'Enter name for player {i+1}: ')
            player = Hand(self.deck.draw(), self.deck.draw(), name) #create players
            self.players.append(player)

    def game_over(self, player):
        score = player.score()
        if score > 21:
            return 'Busted'
        elif score == 21:
            return 'Blackjack!'
        return False
        
    def play(self):
        game_over = False
        while not game_over:

            print('Dealers hand: ')
            print(self.dealer)
            print(f"Dealers score: {self.dealer.visible_score()}")
            players_move = []

            #ask player's moves
            for i in range(len(self.players)):
                player = self.players[i]
                if player.game_over:
                    print(player.game_over)
                    continue
                print()
                print(f'{player.name}''s hand' )
                print(f"{player.name}''s score: {player.score()}")
                
                while True:
                    move = input('(h)it or (s)tay:').strip().lower()
                    if move in ['h', 'hit','s', 'stay']:
                        break
                        
                players_move.append(move)

                if game_over:
                    break
                        
                if move.startswith('h'):
                    card = self.deck.draw()
                    player.add(card)

                # check if game is over for individual player
                player.game_over = self.game_over(player)
                if player.game_over:
                    print(player.game_over)
                
            #calculate dealers moves
            score = self.dealer.score()
            
            if (17 < score < 21):
                print('dealer stays')
            else:
                print('dealer hits ')
                card = self.deck.draw()
                self.dealer.add(card)
                print(card)
                self.dealer.game_over = self.game_over(self.dealer)
                if self.dealer.game_over:
                    print(self.dealer.game_over(self.dealer))
                    break
                print(self.game_over(self.dealer))
            if ('hit' not in players_move) and ('h' not in players_move):
                game_over = True
        # calculate winner
        
        for player in self.players:
            print()
            print(f'{player.name}''s hand')
            print(f"{player.name}''s score: {player.score()}")
            
            if player.score() > 21:
                print(player.name + ' busted' )
            elif player.score() >=self.dealer.score():
                print(player.name + ' wins!')
            elif player.score() == self.dealer.score():
                print(player.name + ' pushes') 
            elif player.score() < self.dealer.score() <= 21:
                print(player.name + ' loses')  
            else:
                print(player.name + ' loses')
        # print(game_over)

if __name__ == '__main__':
    # num_players = input('How many players?: ')
    game = Game(2)
    game.play()
    # for player in game.players:
    #     print(player)
    #     print(player.score())
    # print(game.dealer)
    # print(game.dealer.visible_score())
    # print(game.dealer.score())
    


            

    
            
