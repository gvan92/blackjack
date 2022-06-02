"""
Gregory Van

Description: Objects included are Card, Deck, and Hand. These will be used to build a simple blackjack program.
"""

#!/usr/bin/env python3
import random
CARDS_CHARACTERS = {"Spades": "♠", "Hearts": "♥", "Diamonds": "♦", "Clubs": "♣"}


##########################################################################
## Definitions for the classes: Card, Deck and Hand
##########################################################################

class Card:
    def __init__(self, rank, suit):
            self.rank = rank
            self.suit = suit

    @property
    def value(self):
        if self.rank == 'Ace':
            value = 11
        elif self.rank in ('King', 'Queen', 'Jack'):
            value = 10
        else:
            value = int(self.rank)
        return value

    # def displayCard(self):
    #     return(str(self.rank), 'of', str(self.suit), CARDS_CHARACTERS[self.suit])

    #Make comparable by suit and rank
    RANKORDER = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

    def __eq__(self, other):
        return(self.suit == other.suit and Card.RANKORDER[self.rank] == Card.RANKORDER[other.rank])

    def __lt__(self, other):
        if self.suit == other.suit:
            return (Card.RANKORDER[self.rank] < Card.RANKORDER[other.rank])
        else:
            return (self.suit < other.suit)

    #Make the card class printable
    def __str__(self):
        return(str(self.rank) + ' of ' + str(self.suit) + ' ' + CARDS_CHARACTERS[self.suit])

class Deck:
    def __init__(self):
        self.__deck = []
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        for rank in ranks:
            for suit in suits:
                self.__deck.append(Card(rank, suit))
    
    # @property
    # def count(self):
    #     return len(self.__deck)

    def shuffle(self):
        random.shuffle(self.__deck)
    
    def dealCard(self):
        card = self.__deck[0]
        self.__deck.remove(self.__deck[0])
        return card

    def __iter__(self):
        for card in self.__deck:
            yield card

    def __len__(self):
	    return len(self.__deck)


class Hand:
    def __init__(self):
        self.__cards = []
    
    # @property
    # def count(self):
    #     return len(self.__cards)

    @property
    def points(self):
        points = 0
        for card in self.__cards:
            points += card.value
        return points
    
    def addCard(self, card):
        self.__cards.append(card)

    def __iter__(self):
        for card in self.__cards:
            yield card

    def __len__(self):
	    return len(self.__cards)

        
def main():
    print("Cards - Tester")
    print()

    #test sorting of the cards
    testcardsList = [Card("Ace","Spades"), Card("Queen","Hearts"), Card("10","Clubs"),
             Card("3","Diamonds"), Card("Jack","Hearts"), Card("7","Spades")]
    testcardsList.sort()
    print("TEST CARDS LIST AFTER SORTING.")
    for c in testcardsList:
        print(c)
    print()

    # test deck
    print("DECK")
    deck = Deck()
    print("Deck created.")
    deck.shuffle()    
    print("Deck shuffled.")
    print("Deck count:", len(deck))
    print()

    # test hand
    hand = Hand()
    for i in range(10):
        hand.addCard(deck.dealCard())

    print("SORTED HAND")
    for c in sorted(hand):
        print(c)

    print()
    print("Hand points:", hand.points)
    print("Hand count:", len(hand))
    print("Deck count:", len(deck))

if __name__ == "__main__":
    main()
