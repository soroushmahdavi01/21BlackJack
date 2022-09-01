
################################ IMPORTS ###################################

from operator import contains
import pygame, sys, random
pygame.init()
pygame.font.init()

#######################################

class dealersHand():
    def __init__(self, hidden, shown):
        self.__dealers_total = 0
        self.__dealer_hidden = hidden
        self.__dealer_shown = shown
    def set_dealer_hand(self, score, hidden, shown):
        self.__dealers_total = score
        self.__dealer_hidden = hidden
        self.__dealer_shown = shown
    def get_dealers_total(self):
        if self.__dealer_hidden in ["J", "Q", "K"]:
            self.__dealer_hidden = 10
        if self.__dealer_shown in ["J", "Q", "K"]:
            self.__dealer_shown = 10
        if self.__dealer_hidden == "A": 
            if 11 + self.__dealer_shown > 21:
                return 1 + self.__dealer_shown
            else:
                pass
        return self.__dealers_total
    def get_dealer_hidden(self):
        return self.__dealer_hidden
    def get_dealer_shown(self):
        return self.__dealer_shown
    def __str__(self):
        return f"The Dealers hand shows a {self.__dealer_shown} but hides a {self.__dealer_hidden}"
    
    
         
class usersHand():
    def __init__(self, userFirstCard, userSecondCard):
        self.__users_total = 0
        self.__user_first_card = userFirstCard
        self.__user_second_card = userSecondCard
    def set_user_hand(self, userFirstCard, userSecondCard):
        self.__user_first_card = userFirstCard
        self.__user_second_card = userSecondCard
    def set_user_score(self, score):
        self.__users_score = score
    def get_users_total(self):
        return self.__users_total
    def get_user_first_card(self):
        return self.__user_first_card
    def get_user_second_card(self):
        return self.__user_second_card
    def __str__(self):
        return f"You have a {self.__user_first_card} and a {self.__user_second_card}"

###############################################################

deck = 4*["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
dealerHidden = random.choice(deck)
dealerShown = random.choice(deck)
userFirstCard = random.choice(deck)
userSecondCard = random.choice(deck)

userHand = []
userHand += str(userFirstCard)
userHand += str(userSecondCard)

dealerHand = []
dealerHand += str(dealerHidden)
dealerHand += str(dealerShown)

############################ FUNCTIONS #####################################

def checkScore(cards):
    total = 0
    for i in cards:
        if i in ["J", "Q", "K"]:
            total += 10
        elif i == "A":
            total += 11
        elif i == "0":
            total += 9
        else:
            total += int(i)
    if total > 21:
        total -= 10
        # if total > 21:
        #     total = checkAce(total, cards)
        #     if total == 0:
        #         return "Print"
                
    return total

def getCard(hand):
    hitCard = random.choice(deck)
    hand += str(hitCard)
    if (checkScore(hand) > 21) and hitCard == "A":
        hand -= 10
    return hand ########## what if i check for 21 bust or ace here???

def checkAce(total, cards):
    if total > 21:
        if (i in cards in ["A"]):
            total -= 9
    return total


########################

dealer = dealersHand(dealerHidden, dealerShown)
print(dealer)
user = usersHand(userFirstCard, userSecondCard)
print(user)
print(userHand)
userScore = checkScore(userHand)
print(userScore)
userHand = getCard(userHand)
print(userHand)
userScore = checkScore(userHand)
print(userScore)






