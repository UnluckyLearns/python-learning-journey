class Items():
    def __init__(self):
        pass


class HealthPot(Items):
    def __init__(self):
        self.heal = 15
        self.name = "Health Pot"
        self.cost = 250

class Bomb(Items):
    def __init__(self):
        self.damage = 20
        self.name = "Bomb"
        self.cost = 350
    
    def use(self,monster):
        monster.hp -= self.damage
        print("You Have Used A Bomb and Dealt " + str(self.damage) + " Damage To The Enemy.  ")