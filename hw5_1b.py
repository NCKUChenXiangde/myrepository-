
#統計系116陳祥德H24124068
import random

# (a) 預處理: 創建一副洗好的牌
def create_deck():
    ranks = ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']
    suits = ['SPADE', 'HEART', 'DIAMOND', 'CLUB']
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)  # 洗牌
    return deck

# (b) 安排場地: 發送玩家和莊家的第一張牌
def deal_initial_cards(deck):
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    return player_hand, dealer_hand

# (c) 計算總值: 計算手中牌的總值
def calculate_total(hand):
    total = 0
    ace_count = 0
    for card in hand:
        rank = card[0]
        if rank in ['JACK', 'QUEEN', 'KING']:
            total += 10
        elif rank == 'ACE':
            ace_count += 1
            total += 11
        else:
            total += int(rank)
    # 處理ACE的值
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1
    return total

# (d) 遊戲邏輯: 玩家的hit或stay操作，以及莊家的操作
def player_turn(deck, player_hand, player_draw_cards):
    while True:
        print("Player's hand:", player_hand)
        print("Player's draw cards:", player_draw_cards)
        player_total = calculate_total(player_hand)
        print("Player's total:", player_total)
        if player_total > 21:
            print("Player busts!")
            return 'bust'
        choice = input("Do you want to hit (1) or stay (0)? ")
        if choice == '1':
            drawn_card = deck.pop()
            player_hand.append(drawn_card)
            player_draw_cards.append(drawn_card)
        else:
            return 'stay'

def dealer_turn(deck, dealer_hand, dealer_draw_cards):
    while calculate_total(dealer_hand) < 17:
        drawn_card = deck.pop()
        dealer_hand.append(drawn_card)
        dealer_draw_cards.append(drawn_card)

# (e) 確定贏家
def determine_winner(player_hand, dealer_hand):
    player_total = calculate_total(player_hand)
    dealer_total = calculate_total(dealer_hand)

    if player_total > 21:
        return 'dealer'
    elif dealer_total > 21:
        return 'player'
    elif player_total == dealer_total:
        return 'tie'
    elif player_total == 21 and len(player_hand) == 2:
        return 'player_blackjack'
    elif dealer_total == 21 and len(dealer_hand) == 2:
        return 'dealer_blackjack'
    elif player_total > dealer_total:
        return 'player'
    else:
        return 'dealer'

# (f) 詢問玩家是否繼續遊戲
def play_again():
    while True:
        choice = input("Do you want to play again? (yes/no) ").lower()
        if choice == 'yes':
            return True
        elif choice == 'no':
            return False
        else:
            print("Please enter 'yes' or 'no'.")

# 主程式
while True:
    deck = create_deck()
    player_hand, dealer_hand = deal_initial_cards(deck)
    player_draw_cards = []
    dealer_draw_cards = []
    print("Player's hand:", player_hand)
    print("Dealer's hand:", dealer_hand)

    if player_turn(deck, player_hand, player_draw_cards) == 'bust':
        print("Dealer wins!")
    else:
        dealer_turn(deck, dealer_hand, dealer_draw_cards)
        print("Player's hand:", player_hand)
        print("Dealer's hand:", dealer_hand)
        winner = determine_winner(player_hand, dealer_hand)
        if winner == 'player':
            print("Player wins!")
        elif winner == 'dealer':
            print("Dealer wins!")
        else:
            print("It's a tie!")

    if not play_again():
        print("Thanks for playing!")
        break
