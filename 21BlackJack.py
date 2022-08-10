################################ IMPORTS ###################################

from classes import *
import pygame
import sys
import random

###############################################################

Deck = 4*["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
DealerHidden = random.choice(Deck)
DealerShown = random.choice(Deck)

############################ FUNCTIONS #####################################

dealer = dealersHand(DealerHidden, DealerShown)
print(dealer)