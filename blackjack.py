"""
Gregory Van

Description: The project is to build a card game. The game is a simplified version of the Blackjackgame. 
"""

#!/usr/bin/env python3

from objects import Card, Deck, Hand

class Blackjack:
    def __init__(self, startingBalance):
        self.money = startingBalance
        self.deck = Deck()
        self.playerHand = Hand()
        self.dealerHand = Hand()
        self.bet = 0

    def displayCards(self,hand, title):
        ''' Print the title and display the cards in the given hand in a sorted order'''
        print(title.upper())        
        for c in sorted(hand):
            print(c)
        print()

    def handle_winner(self, winner, message):
        ''' print the player's hand's points
        print the message
        Update self.money according to the winner
        '''
        print('YOUR POINTS: ' + str(self.playerHand.points))
        print(message)
        if winner == "player":
            self.money += self.bet
        elif winner == "dealer":
            self.money -= self.bet
        elif winner == "blackjack":
            self.money += 1.5 * self.bet
        else:
            print ("The winner is invalid")

    def getBet(self):
        ''' Method to update self.bet by prompting the user for the bet amount,
        making sure bet is less than self.money.
        '''
        while True:
            try:
                bet = int(input("Enter bet amount: "))
                if bet < 0:
                    print("Bet must be positve")
                elif bet <= self.money:
                    self.bet = bet
                    return False
                else:
                    print("Bet amount must be less than or equal to current balance.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")

    def setupRound(self):
        ''' Setup the round by doing these steps:
        Call getBet to initialize self.bet,
        initialize self.deck to a new Deck object and shuffle it
        initialize self.dealerHand and self.playerHand to new Hand objects
        deal two cards to the playerHand, and one card to the dealerHand
        finally, print dealerHand and playerHand using displayCards method
        '''
        self.getBet()
        self.deck = Deck()
        self.deck.shuffle()
        self.playerHand = Hand()
        self.dealerHand = Hand()
        for i in range(2):
            self.playerHand.addCard(self.deck.dealCard())
        self.dealerHand.addCard(self.deck.dealCard())
        print()
        self.displayCards(self.dealerHand, "Dealers's Show Hand")
        self.displayCards(self.playerHand, "Your Cards")

    def play_playerHand(self):
        ''' Method to implement player playing his hand by
        1. Prompting the user to indicate Hit (h) or Stand (s)
        2. If user picks stand, end the player play by returning
        3. If user picks hit,
            deal a card to the playerHand.
            check if with the latest addition, the hand busts (has > 21 points), if so return
            otherwise, prompt the player again whether to hit or stand.
        4. Print playerHand points
        '''

        i = True
        while i == True:
            move = str(input("Hit or Stand? (h for hit or s for stand): "))
            print()
            if move == 's':
                i = False
            elif move == 'h':
                self.playerHand.addCard(self.deck.dealCard())
                self.displayCards(self.playerHand, "Your Cards")
                if self.playerHand.points > 21:
                    i =  False
            else:
                print("Invalid option")
        print('YOUR POINTS: ' + str(self.playerHand.points))
    
    def play_dealerHand(self):
        ''' Method to play the dealer's hand.
        Continue to deal cards till the points of the dealerHand are
        equal to or greater than 17. Print the dealer's hand before returning'''
        i = True
        while i == True:
            self.dealerHand.addCard(self.deck.dealCard())
            if self.dealerHand.points >= 17:
                i = False
        self.displayCards(self.dealerHand, "Dealer Cards") 
        print('YOUR POINTS: ' + str(self.playerHand.points))
        print("DEALER'S POINTS: " + str(self.dealerHand.points))
        
    def playOneRound(self):
        ''' Method implements playing one round of the game
        1. Checks if playerHand is a Blackjack, if so handles that case
        2. Lets player play his hand if it busts, declares player loser
        3. Else lets dealer play his hand.
        4. If dealer busts, declares the player to be the winner
        5. Otherwise declares the winner based on who has higher points:
            if Player > dealer, player is the winner
            else if player < dealer, dealer is the winner
            else it is a tie        
        '''
        if self.playerHand.points == 21:
            self.handle_winner("blackjack", "Blackjack! You Win!")
        else:
            self.play_playerHand()
            if self.playerHand.points > 21:
                self.handle_winner("dealer", "Sorry. You busted. You lose.")
            else:
                self.play_dealerHand()
                print()
                if self.dealerHand.points > 21:
                    self.handle_winner("player", "Yay! The dealer busted. You win!")
                elif self.playerHand.points > self.dealerHand.points:
                    self.handle_winner("player", "Hooray! You win!")
                elif self.playerHand.points < self.dealerHand.points:
                    self.handle_winner("dealer", "Sorry. You lose.")
                elif self.playerHand.points == self.dealerHand.points:
                    print("You push.")
                else:
                    print("System Error")
        print("New balance:", self.money)


def main():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")

    # initialize starting money
    money = 100
    print("Starting Balance:", money)

    blackjack = Blackjack(money)
    # start loop
    again = 'y'
    while again.lower() == 'y':

        print("Setting up a round...")
        blackjack.setupRound()

        print("Playing a round...")
        blackjack.playOneRound()

        print()

        while True:
            response = input("Play again? (y/n): ").lower()
            print()
            if response == "n":
                again = response
                break
            elif response == "y":
                break
            else:
                print("Invalid entry. Please enter 'y' or 'n'.")

    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
