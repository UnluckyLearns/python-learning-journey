
class Monster():
    def __init__(self):
        self.hp = 0
        self.maxhp = 0
        self.attack = 10
        self.gold = 0
        self.xp = 0
    def attack_player(self,player):
        player.hp -= round((self.attack / player.deff))
        print("You Have Lost " + str(round((self.attack / player.deff)))  + " HP")

class Goblin(Monster):
    def __init__(self):
        super().__init__()
        self.name = "Goblin"
        self.power = 1.5
        self.hp = 80
        self.maxhp = 80
        self.gold = 100
        self.xp = 30

class Skeleton(Monster):
    def __init__(self):
        super().__init__()
        self.name = "Skeleton"
        self.power = 2
        self.hp = 100
        self.maxhp = 100
        self.gold = 150
        self.xp = 40

class Orc(Monster):
    def __init__(self):
        super().__init__()
        self.name = "Orc"
        self.power = 3
        self.hp = 150
        self.maxhp = 150
        self.gold = 200
        self.xp = 60


class Dragon(Monster):
    def __init__(self):
        super().__init__()
        self.name = "Dragon"
        self.power = 5
        self.hp = 150
        self.maxhp = 350
        self.gold = 400
        self.xp = 100
        self.fire = 30