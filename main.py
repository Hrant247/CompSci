import random
from random import shuffle

global Spades
global Clubs
global Hearts
global Diamonds
global player_hand
global dealer_hand
Spades = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
Clubs = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
Hearts = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
Diamonds = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
player_hand = []
dealer_hand = []
global card_values
global player_score
global dealer_score
global suit_symbol
player_score = 0
dealer_score = 0
card_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "X":10, "J":10, "Q":10, "K":10}
player_hand_values = []
dealer_hand_values = []

name = input('\nHello dear player,\n\n\nThis is a programmed game of Blackjack.\n\n\nPlease enter your name here:')

def redeal():
    global Spades
    global Clubs
    global Hearts
    global Diamonds
    Spades = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "X", "J", "Q", "K"]
    Clubs = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "X", "J", "Q", "K"]
    Hearts = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "X", "J", "Q", "K"]
    Diamonds = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "X", "J", "Q", "K"]
    player_hand.clear()
    dealer_hand.clear()
    global card_values
    global player_score
    global dealer_score
    global suit_symbol
    player_score = 0
    dealer_score = 0
    card_values = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "X": 10, "J": 10, "Q": 10,"K": 10}
    player_hand_values.clear()
    dealer_hand_values.clear()

def shuffle():
    random.shuffle(Spades)
    random.shuffle(Clubs)
    random.shuffle(Hearts)
    random.shuffle(Diamonds)

def hit():
    suit = random.randint(0, 3)
    global card_values
    global player_score
    global suit_symbol
    global card
    global dealer_score
    global suit_symbol
    global card
    if suit == 0:
        suit_symbol = '♠'
        card = Spades[0]
        print_card()
        player_hand.append(card)
        Spades.remove(card)
        x = card_values.get(card)
        player_hand_values.append(x)
        player_score = sum(player_hand_values)
    if suit == 1:
        suit_symbol = '♣'
        card = Clubs[0]
        print_card()
        player_hand.append(card)
        Clubs.remove(card)
        x = card_values.get(card)
        player_hand_values.append(x)
        player_score = sum(player_hand_values)
    if suit == 2:
        suit_symbol = '♥'
        card = (Hearts[0])
        print_card()
        player_hand.append(card)
        Hearts.remove(card)
        x = card_values.get(card)
        player_hand_values.append(x)
        player_score = sum(player_hand_values)
    if suit == 3:
        suit_symbol = '♦'
        card = (Diamonds[0])
        print_card()
        player_hand.append(card)
        Diamonds.remove(card)
        x = card_values.get(card)
        player_hand_values.append(x)
        player_score = sum(player_hand_values)

def deal_hit():
    suit = random.randint(0, 3)
    global card_values
    global player_score
    global suit_symbol
    global dealer_score
    global card
    if suit == 0:
        suit_symbol = '♠'
        card = Spades[0]
        print_card()
        dealer_hand.append(card)
        Spades.remove(card)
        y = card_values.get(card)
        dealer_hand_values.append(y)
        dealer_score = sum(dealer_hand_values)
    if suit == 1:
        suit_symbol = '♣'
        card = Clubs[0]
        print_card()
        dealer_hand.append(card)
        Clubs.remove(card)
        y = card_values.get(card)
        dealer_hand_values.append(y)
        dealer_score = sum(dealer_hand_values)
    if suit == 2:
        suit_symbol = '♥'
        card = (Hearts[0])
        print_card()
        dealer_hand.append(card)
        Hearts.remove(card)
        y = card_values.get(card)
        dealer_hand_values.append(y)
        dealer_score = sum(dealer_hand_values)
    if suit == 3:
        suit_symbol = '♦'
        card = (Diamonds[0])
        print_card()
        dealer_hand.append(card)
        Diamonds.remove(card)
        y = card_values.get(card)
        dealer_hand_values.append(y)
        dealer_score = sum(dealer_hand_values)

def deal():
    shuffle()
    print("Dealer's Cards:")
    deal_hit()
    print(name + "'s Cards:")
    hit()
    hit()
    print("Dealer's Score:", dealer_score)
    print(name + "'s Score:", player_score)

def print_card():
    print('╒═════════════╕')
    print(f'│{card}            │')
    print('''│             │
│             │''')
    print(f'│      {suit_symbol}      │')
    print('''│             │
│             │''')
    print(f'│            {card}│')
    print('╘═════════════╛')

print('''
 __        __   _                            _          ____  _            _     _            _    _ 
 \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   | __ )| | __ _  ___| | __(_) __ _  ___| | _| |
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  |  _ \| |/ _` |/ __| |/ /| |/ _` |/ __| |/ / |
   \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |_) | | (_| | (__|   < | | (_| | (__|   <|_|
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |____/|_|\__,_|\___|_|\_\/ |\__,_|\___|_|\_(_)
                                                                              |__/
''')

print('''
    ____               ___         ___ ___           ___  ___               ___            ___                 
  / ____|              | |         | | | |           | |  | |               | |     ___    | |                                           
 | |     _ __ ___  __ _| |_ ___  __| | | |__  _   _  | |__| |_ __ __ _ _ __ | |_   ( _ )   | |     __ ___      ___ __ ___ _ __   ___ ___ 
 | |    | '__/ _ \/ _` | __/ _ \/ _` | | '_ \| | | | |  __  | '__/ _` | '_ \| __|  / _ \/\ | |    / _` \ \ /\ / / '__/ _ \ '_ \ / __/ _ /
 | |____| | |  __/ (_| | ||  __/ (_| | | |_) | |_| | | |  | | | | (_| | | | | |_  | (_>  < | |___| (_| |\ V  V /| | |  __/ | | | (_|  __/
  \_____|_|  \___|\__,_|\__\___|\__,_| |_.__/ \__, | |_|  |_|_|  \__,_|_| |_|\__|  \___/\/ |______\__,_| \_/\_/ |_|  \___|_| |_|\___\___|
                                               __/ |                                                                                     
                                              |___/     
''')
print("Type 'help' for the commands to play this game!")
while True:
    command = input('>').lower()
    if command == 'help':
        print('''
        rules - rules of the game Blackjack
        start - start a game
        quit - to end and quit the game
        hit - to hit a card
        stand - to end your turn''')
        command = input('>').lower()
    if command == 'rules':
        print('''This Blackjack is a single player game where the player plays against the dealer.\n
        The dealer deals a card, your goal as the player is to try to get to as close to 21 without exceeding it.\n
        You can do this by hitting. Preforming a hit tells the dealer to place another card.\n
        You may also preform a stand. Stand means that you don't want to add anymore cards to your own hand.\n
        After you stand the dealer reveals his cards , where he has been playing the same game as you!\n
        Whichever person is closer to 21 wins! If you or the dealer go over 21, you lose. If its a tie,\n
        nothing happens. In Blackjack an ace can be a 1 or an 11 depending on your hand.''')
        command = input('>').lower()
    if command == 'quit':
        break
    if command == 'start':
        redeal()
        deal()
        start_command = input('>').lower()
        while True:
            if start_command == 'hit':
                hit()
                if player_score < 21:
                    print("Dealer's Score:", dealer_score)
                    print(name + "'s Score:", player_score)
                    start_command = input('>').lower()
                if player_score > 21:
                    if 'A' in player_hand:
                        player_score -= 10
                        print("Dealer's Score:", dealer_score)
                        print(name + "'s Score:", player_score)
                        player_hand.remove('A')
                        player_hand_values.remove(11)
                        player_hand_values.append(1)
                        start_command = input('>').lower()
                    else:
                        print('Dealer Score:', dealer_score)
                        print('Player Score:', player_score)
                        print('DEALER WINS!!!')
                        break
                if player_score == 21:
                    if player_score == dealer_score:
                        print("Dealer's Score:", dealer_score)
                        print(name + "'s Score:", player_score)
                        print('TIE GAME')
                        break
                    else:
                        print("Dealer's Score:", dealer_score)
                        print(name + "'s Score:", player_score)
                        print('YOU HAVE BLACKJACK!!!')
                        break
            elif start_command == 'help':
                print('''
                rules - rules of the game Blackjack
                start - start a game
                quit - to end and quit the game
                ''')
            elif start_command == 'rules':
                print('''This Blackjack is a single player game where the player plays against the dealer.\n
                The dealer deals a card, your goal as the player is to try to get to as close to 21 without exceeding it.\n
                You can do this by hitting. Preforming a hit tells the dealer to place another card.\n
                You may also preform a stand. Stand means that you don't want to add anymore cards to your own hand.\n
                After you stand the dealer reveals his cards , where he has been playing the same game as you!\n
                Whichever person is closer to 21 wins! If you or the dealer go over 21, you lose. If its a tie,\n
                nothing happens. In Blackjack an ace can be a 1 or an 11 depending on your hand.         
                ''')
                break
            elif start_command == 'quit':
                print('''Are you sure you want to quit? 
                This program will shutdown.
                (type quit to confirm)''')
                break
            elif start_command == 'stand':
                while dealer_score < 17:
                    deal_hit()
                if player_score == dealer_score:
                    print("Dealer's Score:", dealer_score)
                    print(name + "'s Score:", player_score)
                    print('TIE GAME')
                    break
                if player_score == 21:
                    if player_score == dealer_score:
                        print("Dealer's Score:", dealer_score)
                        print(name + "'s Score:", player_score)
                        print('TIE GAME')
                        break
                    else:
                        print("Dealer's Score:", dealer_score)
                        print(name + "'s Score:", player_score)
                        print(name + ' HAS BLACKJACK!!!')
                        break
                if dealer_score == 21:
                    if player_score == dealer_score:
                        print("Dealer's Score:", dealer_score)
                        print(name + "'s Score:", player_score)
                        print('TIE GAME')
                        break
                    else:
                        print("Dealer's Score:", dealer_score)
                        print(name + "'s Score:", player_score)
                        print('DEALER HAS BLACKJACK!!!')
                        break
                if player_score > 21:
                    if 'A'in player_hand:
                        player_score -= 10
                        print("Dealer's Score:", dealer_score)
                        print(name + "'s Score:", player_score)
                        player_hand.remove('A')
                        player_hand_values.remove(11)
                        player_hand_values.append(1)
                        start_command = input('>').lower()
                    else:
                        print("Dealer's Score:", dealer_score)
                        print(name + "'s Score:", player_score)
                        print('DEALER WINS!!!')
                        break
                if player_score < 21:
                    if player_score > dealer_score:
                        print("Dealer's Score:", dealer_score)
                        print(name + "'s Score:", player_score)
                        print(name + ' WINS!!!')
                        break
                    if player_score < dealer_score:
                        if dealer_score > 21:
                            if 'A'in dealer_hand:
                                dealer_score -= 10
                                print("Dealer's Score:", dealer_score)
                                print(name + "'s Score:", player_score)
                                dealer_hand.remove('A')
                                dealer_hand_values.remove(11)
                                dealer_hand_values.append(1)
                                start_command = input('>').lower()
                            else:
                                print("Dealer's Score:", dealer_score)
                                print(name + "'s Score:", player_score)
                                print(name + ' WINS!!!')
                                break
                        if dealer_score < 21:
                            print("Dealer's Score:", dealer_score)
                            print(name + "'s Score:", player_score)
                            print('DEALER WINS!!!')
                            break
            elif start_command == 'start':
                redeal()
                deal()
                start_command = input('>').lower()
            else:
                print("Sorry, I don't understand")
                start_command = input('>').lower()
    else:
        print("Sorry, I don't understand")
