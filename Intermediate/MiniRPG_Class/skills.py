

class Skills():
    def __init__(self):
        self.cost = 0
        self.damage =  0 
        self.heal = 0
        self.name = ""
        self.cd = 0
        self.track = 0
    def use(self):
        print(self.name + " Used")



class FireBall(Skills):
    def __init__(self):
        super().__init__()
        self.name = "Fire Ball" 
        self.cost =  20
        self.damage = 40
        self.cd = 3
        self.track = 3
    def use(self,player,monster):
        monster.hp -=  self.damage
        player.mana -= self.cost
        monster.attack_player(player)

class IceSpear(Skills):
    def __init__(self):
        super().__init__()
        self.name = "Ice Spear"
        self.cost =  40
        self.damage = 30
        self.cd = 2
        self.track = 2
    def use(self,player,monster):
        monster.hp -=  self.damage
        player.mana -= self.cost
        monster.attack_player(player)

class Fortify(Skills):
    def __init__(self):
        super().__init__()
        self.name = "Fortify"
        self.buff = 2
        self.cd = 1
        self.track = 1
    def use(self,player,monster):
        player.attack = self.buff  * player.attack
        monster.attack_player(player)
