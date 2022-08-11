
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
    def set_user_hand(self, score, userFirstCard, userSecondCard):
        self.__users_total = score
        self.__user_first_card = userFirstCard
        self.__user_second_card = userSecondCard
    def get_users_total(self):
        return self.__users_total
    def get_user_first_card(self):
        return self.__user_first_card
    def get_user_second_card(self):
        return self.__user_second_card
    def __str__(self):
        return f"You have a {self.__user_first_card} and a {self.__user_second_card}"
    
        
        
        