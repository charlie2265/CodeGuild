import random
class Card:
    def __init__(self, rank, suit):
        ''' create a class that represent a card with the
         value of rank and suit.
         '''
        self.rank = rank
        self.suit = suit
    def __repr__(self):
        return f'Card({self.rank}, {self.suit})'
card = Card('A', 'spades')
# print(card)

class Deck:
    '''a class with one property - a list of cards'''
    def __init__(self):
        ranks = list('A23456789')  + ['10'] + list('JKQ')
        suits =['clubs', 'diamonds', 'hearts', 'spades']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks] #comprehension/

    def __str__(self):
        return str(self.cards)

    def __getitem__(self, idx):
        return self.cards[idx]

    def __len__(self):
        return len(self.cards)

    def draw(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

    def cut(self):
        index = random.randint(0,len(self.cards)-1)
        print(index)

        top = self.cards[index:]
        bottom = self.cards[:index]
        self.cards = top + bottom
        print(self.cards)

if  __name__ == '__main__':

    deck = Deck()
    print(deck.cards)
    print(deck[0])
    print(len(deck))
    print(deck.draw())
    print(len(deck))
    print(deck)
    deck.shuffle()
    print(deck)
    deck.cut()
    print(deck)
