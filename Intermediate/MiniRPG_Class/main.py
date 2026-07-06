from player import Warrior,Mage
from monster import Monster,Goblin,Skeleton,Orc,Dragon
from items import HealthPot,Bomb
from Interfaces import HealthBar,ManaBar
import random
import json
import os

class Game():
    def __init__(self):
        self.player = Warrior()
        self.health_bar1 = HealthBar(self.player,"\033[92m")
        self.mana_bar1 = ManaBar(self.player)
            
    def melee_attack(self,monster):
        print(self.player.attack)
        self.player.attack_monster(monster)
        monster.attack_player(self.player)
        self.health_bar1.update(self.player)
        self.health_bar2.update(monster)

    def chara_stats(self):
        print(f"Class : {self.player.chara}")
        print(f"Level : {self.player.level}")
        print(f"Gold : {self.player.gold}")
        print(f"XP : {self.player.xp}")


    def draw_bars(self,monster):
            print("Player Hp :")
            self.health_bar1.draw()
            print("Player Mana :")
            self.mana_bar1.draw()
            print("\n\n" + monster.name + " Hp :")
            self.health_bar2.draw()
            print("\n")
    
    def update_bars(self,monster,player):
        self.health_bar1.update(player)
        self.health_bar2.update(monster)
        self.mana_bar1.update(player)
        

    def skill_diplay(self,monster):
        for i,skills in enumerate(self.player.skills):
            print(str(i + 1) +"- "+ skills.name)
        choice = input("Use :")
        if not choice.isdigit() :
            print("Give Me A Number.")
        elif int(choice) > len(self.player.skills) or int(choice) <= 0 :
            print("Number Out Of Range")
        else:
            self.player.use_skill(int(choice)-1,monster)


    def player_select(self):
        while True:
            choice = input("CHOOSE YOUR CLASS: \n\n"
                            "1- Warrior\n"
                            "2- Mage\n" )
            if choice not in ('1','2'):
                print("Invalid Input")
            elif choice == "1":
                self.player = Warrior()
                return
            elif choice == "2":
                self.player = Mage()
                return
    
    def store(self):
        print( "----------------STORE : " +str(self.player.gold) +" GOLD AVAILABLE --------------------")
        while True:
            choice = input(
                "1- Health Pot " + str(HealthPot().cost)+" Gold\n"
                "2- Bomb " +str(Bomb().cost)+ " Gold\n"
                "3- EXIT \n")
            if choice not in ("1","2","3"):
                print("Invalid Input")
            elif choice == "1":
                if self.player.gold >= HealthPot().cost:
                    print("You Have Bought A Health Potion .")
                    self.player.inventory.append(HealthPot())
                    self.player.gold -= HealthPot().cost
                else:
                    print("Not Enought Money")
            elif choice == "2":
                if self.player.gold >= Bomb().cost:
                    print("You Have Bought Bomb .")
                    self.player.inventory.append(Bomb())
                    self.player.gold -= Bomb().cost
                else:
                    print("Not Enought Money")
            elif choice =="3":
                return


    def battle(self):
        if self.player.level != 10:
            monster = random.choice([
                Goblin(),
                Skeleton(),
                Orc()
            ])
        else : 
            monster = Dragon()
        self.health_bar2 = HealthBar(monster,"\033[91m")
        print(monster.name + " Appeared! \n\n")
        while monster.hp > 0 and  self.player.hp > 0:
            self.draw_bars(monster)
            choice = input(
                            "1- Attack\n"
                            "2- Skills\n"
                            "3- Invetory\n"
                            "4- RUN\n")
            if choice not in ("1","2","3","4"):
                print("invalid input")
            if choice == "1":
                self.melee_attack(monster)
            elif choice == "2":
                self.skill_diplay(monster)
                self.update_bars(monster,self.player)
            elif choice == "3":
                self.inventory(monster)
        if self.player.hp <= 0:
            print("You Died.")
            self.player.reset_stats()
            self.update_bars(monster,self.player)
            self.mana_bar1.update(self.player)
            return
        elif monster.hp <= 0:
            if isinstance(monster,Dragon):
                print("---------------CONGRATS YOU HAVE DEFEATED THE FINAL BOSS-----------------------")
                exit()
            print("You Killed " + monster.name)
            self.player.reset_stats()
            self.update_bars(monster,self.player)
            self.player.update_stats(monster)
            return        
        
    
    def inventory(self,monster):
        i = 0
        print( "----------------INVENTOTY--------------------")
        if not self.player.inventory:
            print("Inventory Empty")
            return
        else:

            while True:
                for items in self.player.inventory:
                    print(str(i + 1)  + "- " +items.name)
                    i += 1
                choice = input("Use :")
                inp = int(choice )- 1
                if inp < 0 or inp > i :
                    print("Invalid Input")
                    return
                else:
                    if isinstance(self.player.inventory[inp],HealthPot) :
                        self.player.heal(self.player.inventory[inp])
                        del self.player.inventory[inp]
                        self.health_bar1.update(self.player)
                        self.health_bar2.update(monster)
                    elif isinstance(self.player.inventory[inp],Bomb):
                        self.player.inventory[inp].use(monster)
                        del self.player.inventory[inp]
                        self.health_bar1.update(self.player)
                        self.health_bar2.update(monster)
                    monster.attack_player(self.player)
                    return
                

    def save_chara(self):
        invent = []
        for items in self.player.inventory:
            invent.append(items.name)
        chara_dict  = {"Class" : self.player.chara , "Hp" :self.player.hp  , "Max Hp" : self.player.maxhp ,"Inventory" : invent, "Attack" : self.player.attack ,"Gold" : self.player.gold ,"Level" : self.player.level ,"Deffense" : self.player.deff, "XP": self.player.xp}
        with open(r"C:\Users\User\Desktop\test\MiniRPG_Class\chara.json","w") as file:
            json.dump(chara_dict,file,indent=3)


                

    def new_game(self):
        while True :
            choice = input("-------------- MINI RPG ARENA ------------- \n\n"
                            "1- Explore\n"
                            "2- Shop \n"
                            "3- Character \n"
                            "4- Save Chara \n"
                            "5- Exit \n")
            if  choice not in ("1","2","3","4","5"):
                print("invalid input")
            elif choice == "1":
                ran = random.randint(1,10)
                if ran > 3:
                    self.battle()
                else:
                    print("You Have Encountered Nothing")
            elif choice == "2":
                self.store()
            elif choice == "3":
                self.chara_stats()
            elif choice == "4":
                self.save_chara()
    
    def load_game(self):
        if os.path.isfile(r"C:\Users\User\Desktop\test\MiniRPG_Class\chara.json"):
            with open(r"C:\Users\User\Desktop\test\MiniRPG_Class\chara.json","r") as file:
                chara_dict = json.load(file)
            if chara_dict["Class"] == "Mage":
                self.player = Mage()
            else:
                self.player = Warrior()                
            self.player.attack = chara_dict["Attack"]
            self.player.hp = chara_dict["Hp"]
            self.player.maxhp = chara_dict["Max Hp"]
            self.player.level = chara_dict["Level"]
            self.player.xp = chara_dict["XP"]
            self.player.chara = chara_dict["Class"]
            self.player.gold = chara_dict["Gold"]
            self.player.deff = chara_dict["Deffense"]
            for item in chara_dict["Inventory"]:
                if item == "Health Pot":
                    self.player.inventory.append(HealthPot())
                elif item == "Bomb":
                    self.player.inventory.append(Bomb())
            print(self.player.attack)
            self.new_game()
        else:
            print("No Character saved")
            return
        

    def start_game(self):
        while True :
            choice = input("-------------- MINI RPG ARENA ------------- \n\n"
                            "1- New Game\n"
                            "2- Load game\n"
                            "3- Exit \n")
            if choice not in ("1","2","3"):
                print("invalid input")
            elif choice =="1":
                self.player_select()
                self.new_game()
            elif choice =="2":
                self.load_game()
            elif choice =="3":
                break


def main():
    Game().start_game()

        

if __name__ == "__main__":
    main()