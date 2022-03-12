import random

def play_game():
    input("Press enter to begin\n")
    
    chips=500
    while chips > 0:
        print("Chips remaining: " + str(chips))

        bet= int(input("Enter bet: "))

        check_enough_chips_to_bet(bet, chips)
        
        hand = deal_hand()
        
        score = 0
        for card in hand:
            score += get_score(card)
        print(f"\nYour hand value is: {score}")  

        while score < 21:

            nextcard=str(input("press H to hit or S to stand: "))
            while nextcard.lower() != 'h' and nextcard.lower() != 's':
                nextcard=str(input("Press the right key lol, H to hit or S to stand: "))
            
            if nextcard=='s':
                print(f"You stuck at {score}")
                break

            if nextcard== 'h':
                hand = deal_card(hand)
                print("Players cards: " +  cards_as_string(hand))
                score += get_score(hand[-1])
                print(f"Your hand value is: {score}")
            
        if score == 21:
            print("BLACKJACK PLAYER WINS")
            chips=chips+1.5*bet
        elif score > 21:
            print("BUST COMPUTER WINS")
            chips=chips-bet
    print("You are all out of chips")            
            
def check_enough_chips_to_bet(bet, chips):
    while True:
        if bet <= chips:
            break
        else:
            print("Insufficient chips, chips left: " + chips)
            bet= int(input("Enter bet: "))        

def deal_hand():
    hand=[random.choice(cards)]
    cards.remove(hand[0])
    print(f"\nYou have drawn {hand[0]}")
    hand = deal_card(hand)
    
    return hand

def cards_as_string(hand):
    cards = ""
    for card in hand:
        cards = f"{cards} {card}" 
    return cards

def deal_card(hand: list):
    hand.append(random.choice(cards))
    cards.remove(hand[-1])
    print(f"You have drawn {hand[-1]}")
    return hand

def get_score(card):
    if card[0] in faces:
        return 10
    else:
        return int(card[0])
if __name__ == "__main__":
    cards=['2H','3H','4H','5H','6H','7H','2S','3S','4S','5S','6S','7S','2D','3D','4D','5D','6D','2C','3C','4C','5C','6C','7C']
    # here you can have a dictionary which can call the actual names of the cards to show instead of the 2 characters, e.g. cards_dict['AH'] would return 'Ace of Hearts'
    # cba doing it 52 times rn
    # cards_dict = {'AH': 'Ace of Hearts', 'KH': 'King of Hearts'}
    faces = ['A', 'K', 'Q', 'J', 'T']
    play_game()


