from random import *


#Simple text based Blackjack game demonstrating OOP using Python3


#Creating the deck of cards used. Using Casino rules with 8 decks shuffled together

cards = [1,2,3,4,5,6,7,8,9,10,'J','Q','K']
suites = ['D','C','H','S']
deck = []
player = 1
game = 'Not Over'
dealerMoney = 200
playerMoney = 200

for i in range(0,8):
    for c in cards:
        for s in suites:
            card = str(c) + str(s)
            deck.append(card)



#Shuffle the cards and player 1 chooses placement of deck cut

shuffle(deck)
while True:
    try:
        cutPosition = int(input('Player 1, choose a number between 64 and 75:'))
    except:
        print('That is not a number between 64 and 75.')
    else:
        if 64 <= cutPosition <= 75:
            break
        else:
            print("That is not a number between 64 and 75.")
            continue

#cuts the deck of x number of cards from the botom of the deck determined by the cutPostion variable
deck = deck[0:(416-cutPosition)]



#Game Class. Sets up the core object for game play
up_cards = []
down_cards = []
players = 1
current_player = 0
deal = 'true'


class Game(object):

    startingCash = 200

    def __init__(self, game_deck, players, current_player):
        self.gameDeck = game_deck
        self.players = players
        self.current_player = current_player


    #cards are dealt every other player
    def deal(self):

        on_table = []
        for i in range(0,(self.players + 1)):
            on_table.append(['', ''])

        card_count = 0
        for i in range(0,2):
            player = 0
            for x in range(0, self.players + 1):
                on_table[player][card_count] = self.gameDeck[0]
                del self.gameDeck[0]
                player += 1
            card_count += 1

        return on_table

    def hit(self, current_player):
        global on_table


        on_table[current_player].append(self.gameDeck[0])
        del self.gameDeck[0]

    def stand(self, current_player):
        global player
        global deal

        if current_player == 0:
            print('Dealer Stands')

        else:
            print('You stand.')
            player = 0
            deal = 'false'

    #Allows each player to choose Hit or Stand and deals out cards
    def firstTurnPlayer(self, current_player):

        while True:
            choice = int(input("Press 1 for Hit, 2 for stand."))

            if choice != 1 and  choice != 2:
                print("You need to choose 1 or 2!")


            elif choice == 1:
                print("You Hit.")
                currentGame.hit(current_player)
                # on_table[current_player + 1].append(self.gameDeck[0])
                del self.gameDeck[0]
                break

            elif choice == 2:
                currentGame.stand(current_player)
                break

            else:
                pass



    def cardCounter(self, current_player):

        total = []
        for i in range(0, len(on_table[current_player])):
            c = on_table[current_player][i]
            if len(c) == 3:
                total.append(10)
            elif c[0] == 'J' or c[0] == 'Q' or c[0] == 'K':
                    total.append(10)

            else:
                total.append(int(c[0]))
        return total



    def turnDealer(self):
        global dealer_bust

        print('Dealers Turn')
        print('Dealer has a:', str(on_table[0][0]), 'and a:', str(on_table[0][1]))

        while True:

            DealerCount = sum(currentGame.cardCounter(0))

            if DealerCount > 21:
                print('Dealer Busts with:', DealerCount)
                dealer_bust = True
                break

            elif DealerCount <= 17:
                print('Dealer Hits')
                currentGame.hit(player)
                print('Dealer gets a:', on_table[0][-1])
                print('Dealer has:', sum(currentGame.cardCounter(0)))


            else:
                print('Dealer Stays')
                break

    def compare(self, betAmount):
        global dealer_bust
        global player_bust
        global playerMoney
        global dealerMoney

        dealerCount = sum(currentGame.cardCounter(0))
        playerCount = sum(currentGame.cardCounter(1))
        if dealerCount >= playerCount and dealer_bust != True:
            print("Dealer wins with a:", sum(currentGame.cardCounter(0)))
            playerMoney = playerMoney - betAmount
            dealerMoney = dealerMoney + betAmount

            input("Press any key to continue \n")
        elif player_bust != True:
            print("You win with a:", sum(currentGame.cardCounter(1)))
            print("Dealer had:", sum(currentGame.cardCounter(0)))
            playerMoney = playerMoney + betAmount
            dealerMoney = dealerMoney - betAmount
            input("Press any key to continue \n")
        else:
            pass

