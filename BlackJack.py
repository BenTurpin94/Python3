from optparse import Values
import random
from re import S
from secrets import choice

#from string import capwords
input("Press enter to begin")
Values=[]
cards=['AH','KH','QH','JH','2H','3H','4H','5H','6H','7H','8H','9H','TH','AS','KS','QS','JS','2S','3S','4S','5S','6S','7S','8S','9S','TS','AD','KD','QD','JD','2D','3D','4D','5D','6D','7D','8D','9D','TD','AC','KC','QC','JC','2C','3C','4C','5C','6C','7C','8C','9C','TC']
  
Chips=500
while Chips>0:
    print("Chips remaining=",Chips)

    bet= int(input("Enter bet"))

    while True:
        if bet <= Chips:
            break
        else:
            print("Insufficient Chips, Chips left=",Chips)
            bet= int(input("Enter bet"))
    deal=[]
    deal_player1=random.choice(cards)
    deal.append(deal_player1)
    cards.remove(deal_player1)
    deal_player2=random.choice(cards)
    deal.append(deal_player2)
    cards.remove(deal_player2)
    print("Players cards:",deal_player1,deal_player2)

    values=[deal[0][0],deal[1][0]]
    intvals=[]
    print(values)
    for value in values:
        if value == 'K':
            #print(value)
            intvals.append(int(10))
        elif value == 'Q':
            #print(value)
            intvals.append(int(10))
        elif value == 'J':
            #print(value)
            intvals.append(int(10))
        elif value == 'T':
            
            intvals.append(int(10))
        elif value == 'A':
            intvals.append(int(1))
                # print(value)
        else:
            #print(value)
            intvals.append(int(value))
    add=sum(intvals)
    if add == 21:
        print("BLACKJACK PLAYER WINS")
        Chips=Chips+1.5*bet
    else:
        print("Your hand value is",add)
    nextcard=str(input("press H to hit or S to stand"))
    while nextcard !='h' or 's':
        if nextcard=='s':
            print("You stuck at",add)
            break
        if nextcard== 'h':
            deal_player3=random.choice(cards)
            deal.append(deal_player3)
            cards.remove(deal_player3)
            print("Players cards:",deal_player1,deal_player2,deal_player3)
            print(deal)
            values=[deal[0][0],deal[1][0],deal[2][0]]
            intvals=[]
            print(values)
            for value in values:
                if value == 'K':
                # print(value)
                    intvals.append(int(10))
                elif value == 'Q':
                # print(value)
                    intvals.append(int(10))
                elif value == 'J':
                    #print(value)
                    intvals.append(int(10))
                elif value == 'T':
                    #print(value)
                    intvals.append(int(10))
                elif value == 'A':
                # print(value)
                 intvals.append(int(1))
                else:
                    #print(value)
                    intvals.append(int(value))
            add=sum(intvals)
            if add == 21:
                print("BLACKJACK PLAYER WINS")
                Chips=Chips+bet
                break
            if add > 21:
                print("BUST COMPUTER WINS")
                Chips=Chips-bet
                break
            if add < 21:
                print("Your hand value is",add)
                nextcard1=str(input("press H to hit or S to stand"))
                while nextcard1 !='h' or 's':
                    if nextcard1=='s':
                        print("You stuck at",add)
                        break
                    if nextcard1== 'h':
                        deal_player4=random.choice(cards)
                        deal.append(deal_player4)
                        cards.remove(deal_player4)
                        print("Players cards:",deal_player1,deal_player2,deal_player3,deal_player4)
                        print(deal)
                        values=[deal[0][0],deal[1][0],deal[2][0],deal[3][0]]
                        intvals=[]
                        print(values)
                        for value in values:
                            if value == 'K':
                            # print(value)
                                intvals.append(int(10))
                            elif value == 'Q':
                            # print(value)
                                intvals.append(int(10))
                            elif value == 'J':
                                #print(value)
                                intvals.append(int(10))
                            elif value == 'T':
                                #print(value)
                                intvals.append(int(10))
                            elif value == 'A':
                            # print(value)
                                intvals.append(int(1))
                            else:
                                #print(value)
                                intvals.append(int(value))
                        add=sum(intvals)
                        if add == 21:
                            print("BLACKJACK PLAYER WINS")
                            Chips=Chips+bet
                            break
                        if add > 21:
                            print("BUST COMPUTER WINS")
                            Chips=Chips-bet
                            break
                        if add < 21:
                            print("Your hand value is",add)
                            nextcard2=str(input("press H to hit or S to stand"))
                            while nextcard2 !='h' or 's':
                                if nextcard2=='s':
                                    print("You stuck at",add)
                                    break
                                if nextcard2== 'h':
                                    deal_player5=random.choice(cards)
                                    deal.append(deal_player5)
                                    cards.remove(deal_player5)
                                    print("Players cards:",deal_player1,deal_player2,deal_player3,deal_player5)
                                    print(deal)
                                    values=[deal[0][0],deal[1][0],deal[2][0],deal[3][0],deal[4][0]]
                                    intvals=[]
                                    print(values)
                                    for value in values:
                                        if value == 'K':
                                        # print(value)
                                            intvals.append(int(10))
                                        elif value == 'Q':
                                        # print(value)
                                            intvals.append(int(10))
                                        elif value == 'J':
                                            #print(value)
                                            intvals.append(int(10))
                                        elif value == 'T':
                                            #print(value)
                                            intvals.append(int(10))
                                        elif value == 'A':
                                        # print(value)
                                            intvals.append(int(1))
                                        else:
                                            #print(value)
                                            intvals.append(int(value))
                                    add=sum(intvals)
                                    if add == 21:
                                        print("BLACKJACK PLAYER WINS")
                                        Chips=Chips+bet
                                        break
                                    if add > 21:
                                        print("BUST COMPUTER WINS")
                                        Chips=Chips-bet
                                        break
                                    if add < 21:
                                        print("Your hand value is",add)
                                        nextcard3=str(input("press H to hit or S to stand"))
                                        while nextcard3 !='h' or 's':
                                            if nextcard3=='s':
                                                print("You stuck at",add)
                                                break
                                            if nextcard3== 'h':
                                                deal_player6=random.choice(cards)
                                                deal.append(deal_player6)
                                                cards.remove(deal_player6)
                                                print("Players cards:",deal_player1,deal_player2,deal_player3,deal_player5,deal_player6)
                                                print(deal)
                                                values=[deal[0][0],deal[1][0],deal[2][0],deal[3][0],deal[4][0],deal[5][0]]
                                                intvals=[]
                                                print(values)
                                                for value in values:
                                                    if value == 'K':
                                                    # print(value)
                                                        intvals.append(int(10))
                                                    elif value == 'Q':
                                                    # print(value)
                                                        intvals.append(int(10))
                                                    elif value == 'J':
                                                        #print(value)
                                                        intvals.append(int(10))
                                                    elif value == 'T':
                                                        #print(value)
                                                        intvals.append(int(10))
                                                    elif value == 'A':
                                                    # print(value)
                                                        intvals.append(int(1))
                                                    else:
                                                        #print(value)
                                                        intvals.append(int(value))
                                                add=sum(intvals)
                                                if add == 21:
                                                    print("BLACKJACK PLAYER WINS")
                                                    Chips=Chips+bet
                                                    break
                                                if add > 21:
                                                    print("BUST COMPUTER WINS")
                                                    Chips=Chips-bet
                                                    break
                                                if add < 21:
                                                    print("Your hand value is",add)
                                                break
                                break
                        break    
                break       
        else:
            print("INVALID INPUT")
            nextcard=str(input("press H to hit or S to stand"))
print("You are all out of chips")            
            
        
    

            


