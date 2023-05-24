import random
suits=('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing=True
class Card():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        
    def __str__(self):
        return self.rank +  " of "  + self.suit
class Deck:
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    def __str__(self):
        deck_comp=''
        for card in self.deck:
            deck_comp+='\n' +card.__str__()
        return "The deck has" + deck_comp
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        return self.deck.pop()
class Chips:
    def __init__(self):
        self.total=100
        self.bet=0
    def win_bet(self):
        self.total+=self.bet
    def lose_bet(self):
        self.total-=self.bet
class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
        
    def add_cards(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]
        if card.rank=="Ace":
            self.aces+=1
    def adjust_for_ace(self):
        while self.value>21 and self.aces:
            self.value-=10
            self.aces-=1
def take_bet(chips):
    while True:
        try:
            chips.bet=int(input("how many chips do you wanna bet:"))
        except:
            print("sorry thats invalid")
        else:
            if chips.bet>chips.total:
                print(f'These many chips arent available. You have only {chips.total} chips')
            else:
                break
def hit(deck,hand):
    hand.add_cards(deck.deal())
    hand.adjust_for_ace()
def hit_stand(deck,hand):
    global playing
    while True:
        x=input("\n"+"Do you wanna hit or stand ? 'h' or 's':")
        if x=='h':
            hit(deck,hand)
        elif x=='s':
            print("\n"+"player wants to stand. Dealer's turn")
            playing=False
        else:
            print("\n"+"sorry that was neither a hit nor a stand")
            continue
        break
def show_some(player,dealer):
    print("\n"+"DEALER'S HANDS")
    print("first card hidden")
    print(dealer.cards[1])
    print("\n"+"\n"+"PLAYER'S HANDS")
    for card in player.cards:
        print(card)
def show_all(player,dealer):
    print("\n"+"Dealer's hands")
    for card in dealer.cards:
        print(card)
    print("\n"+f'The value of dealer"s cards is {dealer.value}' )
    print("\n"+"Player's hands")
    for card in player.cards:
        print(card)
    print("\n"+f'The value of player"s cards is {player.value}' )
def player_bust(player,dealer,chips):
    print("\n"+"PLAYER BUSTS")
    chips.lose_bet()
def player_wins(player,dealer,chips):
    print("\n"+"PLAYER WON!!")
    chips.win_bet()
def dealer_busts(player,dealer,chips):
    print("\n"+"DEALER BUSTS! PLAYER WINS!!")
    chips.win_bet()
def dealer_wins(player,dealer,chips):
    print("\n"+"DEALER WON!!")
    chips.lose_bet()
def push(player,dealer):
    print("\n"+"player and dealer TIE!! PUSH!")
while True:
    print("WELCOME TO BLACKJACK")
    deck=Deck()
    deck.shuffle()
    player_hand=Hand()
    
    player_hand.add_cards(deck.deal())
    player_hand.add_cards(deck.deal())
    
    
    dealer_hand=Hand()
    
    dealer_hand.add_cards(deck.deal())
    dealer_hand.add_cards(deck.deal())
    player_chips=Chips()
    take_bet(player_chips)
    show_some(player_hand,dealer_hand)
    while playing:
        hit_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        if player_hand.value>21:
            player_bust(player_hand,dealer_hand,player_chips)
            break
        if player_hand.value<=21:
            while dealer_hand.value<17:
                hit(deck,dealer_hand)
            show_all(player_hand,dealer_hand)
            if dealer_hand.value>21:
                dealer_busts(player_hand,dealer_hand,player_chips)
                break
            elif dealer_hand.value<player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)
                break
            elif dealer_hand.value>player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)
                break
            else:
                push(player_hand,dealer_hand)
    print("\n"+f'Player total chips are {player_chips.total}')
    new_game=input("do you wanna play again? y or n:")
    if new_game=='y':
        playing=True
        continue
    else:
        print("thanks for playing")
        break
        
    
        
    
        
    