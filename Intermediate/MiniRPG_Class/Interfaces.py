import os

os.system ("")

class Interfaces():
    symbol_remaining  = "█"
    symbol_lost = "_"
    barrier = "|"
    def __init__(self):
        pass
    def draw(self):
       remaining_bars = round(self.current_value / self.max_value * self.lenght) 
       lost_bars = self.lenght - remaining_bars
       print(str(self.current_value)+ " // " + str(self.max_value))
       print(self.barrier + 
             self.color +
             str(remaining_bars * self.symbol_remaining)+
             str(lost_bars * self.symbol_lost) +
             "\033[0m" +
             self.barrier)



class HealthBar(Interfaces):

    def __init__(self,player,color):
        self.lenght = 20
        self.max_value =  player.maxhp
        self.current_value = player.hp
        self.color = color
    
    def update(self,player):
        self.current_value = player.hp
    


class ManaBar(Interfaces):
    
    def __init__(self,player):
        self.lenght = 15
        self.max_value =  player.maxmana
        self.current_value = player.mana
        self.color = "\033[34m"

    def update(self,player):
        self.current_value = player.mana