################################ IMPORTS ###################################

from classes import *
import pygame, sys ,random
pygame.init()
pygame.font.init()
gameTrue = pygame.get_init()
print(gameTrue)

###############################################################

deck = 4*["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
dealerHidden = random.choice(deck)
dealerShown = random.choice(deck)
userFirstCard = random.choice(deck)
userSecondCard = random.choice(deck)

############################ FUNCTIONS #####################################

dealer = dealersHand(dealerHidden, dealerShown)
print(dealer)
user = usersHand(userFirstCard, userSecondCard)
print(user)
dealerHidden = random.choice(deck)
dealerShown = random.choice(deck)
dealer = dealersHand(dealerHidden, dealerShown)
print(dealer)

