import random
import json

def reset_stats(player,monster):
        player["HP"] = player["Max HP"]
        monster["HP"]= monster["Max HP"]
        player["Potions"] = player["Max Potions"]

def heal_player(player):
    if player["Potions"] == 0:
            print("No Potions Left")
    elif player["HP"] == player["Max HP"]:
            print("Already Full")
    else: 
            player["Potions"] -= 1
            player["HP"] = min(player["HP"] + player["Potion Power"] , player["Max HP"])

def attack_monster(player,monster):
        attack = random.randint(int(player["Min"]*player["Power"]),int(player["Attack"]*player["Power"]))
        print("You Hit The " + monster["Name"] + " for " + str(attack) + " damage.")
        monster["HP"] = max(0, monster["HP"] - attack)

def take_damage(player,monster):
        attack = random.randint(monster["Min"],monster["Attack"])
        print("You Have Taken " + str(attack) + " Damage This Turn .")
        player["HP"] -= attack

def choose_opp():
    while True:
        choice = input("------------------ Choose The Monster -----------------\n\n"
                    "1- Goblin\n"
                    "2- Skeleton \n"
                    "3- Orc \n")
        if choice != "1" and choice != "2" and choice != "3":
             print("Invalid Input ")
        else:
             return(int(choice)-1)
        


def new_game(player,opp):
    player["Index"] = choose_opp()
    monster = opp["Monsters"][player["Index"]]
    while True:
        print("Player HP : " +str( player["HP"]) + "/" + str(player["Max HP"]))
        print(monster["Name"] + " HP: " + str(monster["HP"]))
        choice = input("1- Attack\n"
                "2- Heal\n")
        if choice != "1" and choice != "2":
            print("Invalid Input ")
        elif choice == "1":
            attack_monster(player,monster)
        elif choice == "2":
            heal_player(player)
        if  monster["HP"] > 0:
            take_damage(player,monster)
        elif  monster["HP"] <= 0:
            print("You Have Defeated The Enemy And Gained " + str(monster["Gold"]) + " Gold")
            reset_stats(player,monster)  
            player["Wins"] += 1
            player["Gold"] += monster["Gold"]
            return
        if player["HP"] <= 0:
            reset_stats(player,monster)
            print("You Have Lost")
            return

def show_stats(player):
    print(player)

def shop(player):
    while True:
        choice = input("------------------ STORE CURENT BUDGET " + str(player["Gold"])+"G "  "-----------------\n\n"
                    "1- Upgrade Attack Power(800 Gold)\n"
                    "2- Upgrade Healing Power(1000 Gold)\n"
                    "3- Upgrade Max Potion Stacks(2500 Gold)\n"
                    "4- Exit\n\n")
        if choice != "1" and choice != "2" and choice != "3" and choice != "4":
            print("Invalid Input ")
        elif choice == "1":
            if player["Gold"] >= 800:
                player["Gold"] -= 800
                player["Power"] += 0.2
                print("You Have Upgraded Your Attacking Power")
            else:
                print("Not Enough Money")
        elif choice == "2":
            if player["Gold"] >= 1000:
                player["Gold"] -= 1000
                player["Potion Power"] += 5
            else:
                print("Not Enough Money")
        elif choice == "3":
            if player["Gold"] >= 2500:
                player["Gold"] -= 2500
                player["Max Potions"] += 1
            else:
                print("Not Enough Money")
        elif choice == "4":
            return


def main():
    player = {"HP": 100,"Max HP": 100,"Attack": 15,"Min" : 10,"Potions": 2,"Wins": 0,"Gold" : 0,"Power" : 1, "Potion Power" : 15,"Max Potions" : 2,"Index":0}
    with open("Monsters.json","r") as file:
         opp = json.load(file)
    print(opp)
    while True:
        choice = input("------------------ Mini RPG -----------------\n\n"
                    "1- New Game\n"
                    "2- View Stats \n"
                    "3- Shop \n"
                    "4- Exit \n")
        if choice != "1" and choice != "2" and choice != "3" and choice != "4":
            print("Invalid Input ")
        elif choice == "1":
            new_game(player,opp)
        elif choice == "2":
            show_stats(player)
        elif choice == "3":
            shop(player)
        elif choice == "4":
             break
if __name__ == "__main__":
    main()