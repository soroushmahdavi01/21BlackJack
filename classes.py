
#######################################

class dealersHand():
    def __init__(self, hidden, shown):
        self.__dealers_total = 0
        self.__dealer_hidden = hidden
        self.__dealer_shown = shown
    def set_dealer_hand(self, hidden, shown):
        self.__dealer_hidden = hidden
        self.__dealer_shown = shown
    def get_dealer_hidden(self):
        return self.__dealer_hidden
    def get_dealer_shown(self):
        return self.__dealer_shown
    def __str__(self):
        return f"The Dealers hand is a {self.__dealer_hidden} and a {self.__dealer_shown}."
    
         
        