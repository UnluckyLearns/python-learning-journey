from skills import Fortify,IceSpear,FireBall

class Player():
    def __init__(self):
        self.chara = ""
        self.hp = 100
        self.maxhp = 100
        self.attack = 12
        self.gold = 0
        self.level = 1
        self.xp = 0
        self.deff = 1
        self.mana = 80
        self.maxmana = 80
        self.inventory = []
        self.skills = []


    def attack_monster(self,monster):
        monster.hp -= self.attack
        self.update_cds()
        print("You Have Dealt " + str(self.attack)  + " Damage.")
    
    def heal(self,potion):
        print ("You Have Healed For : " + str(min(self.maxhp - self.hp , potion.heal)))
        self.update_cds()
        self.hp  = min(self.maxhp,(self.hp + potion.heal))
    
    def update_stats(self,monster):
        self.gold += monster.gold
        self.xp += monster.xp
        print("You Have Gained : " + str(monster.gold) + " Gold And " +  str(monster.xp) + " XP")
        while self.xp  >= 100:
            self.level += 1
            self.xp -= 100
            self.attack += 3
            print("You have Leveled UP : " + "Level " + str(self.level) + "\n\n")
    
    def reset_stats(self):
        self.hp = self.maxhp
        self.mana = self.maxmana
    
    def use_skill(self,index,monster):
        if self.mana < self.skills[index].cost:
            print("Not Enough Mana")
        elif self.skills[index].track != self.skills[index].cd:
            print("Spell ON CD")
        else :
            self.skills[index].use(self,monster)
            self.skills[index].track = 0
            self.update_cds()
    
    def update_cds(self):
        for i,spells in enumerate(self.skills):
            if spells.track != spells.cd:
                self.skills[i].track += 1



class Warrior(Player):
    def __init__(self):
        super().__init__()
        self.deff = 1.2
        self.attack = 14
        self.chara = "Warrior"
        self.skills = [Fortify()]


class Mage(Player):
    def __init__(self):
        super().__init__()
        self.deff = 1.2
        self.attack = 14
        self.chara = "Mage"
        self.skills = [FireBall(),IceSpear()]