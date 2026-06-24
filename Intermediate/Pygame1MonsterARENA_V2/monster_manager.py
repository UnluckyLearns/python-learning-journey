from monster import Monster
import json
import random
import pygame

class MonsterManager():
    def __init__(self):
        with open(r"C:\Users\User\Desktop\test\Pygame1MonsterARENA\monsters.json","r") as file:
            self.monsters = json.load(file)
        self.monster_list = []
        self.wave = 1
    
    def spawn_monster(self):
        self.monster_list = []
        i = 0
        while i < self.wave * 2 :
            monst = random.choice(self.monsters["Monsters"])
            monster = Monster() 
            monster.HP = monst["HP"]
            monster.name = monst["Name"]
            monster.DMG = monst["Damage"]
            monster.color = monst["Color"]
            monster.speed = monst["Speed"]
            self.monster_list.append(monster)
            i +=1 
        return self.monster_list
    
    def move_monster(self,player):
        for monster in self.monster_list:
           
            if player.player[1] - monster.monster[1]  > 0 and not player.player.colliderect(monster.monster): 
                    monster.monster[1] += (1 *  monster.speed)
            if player.player[1] - monster.monster[1]  < 0  and not player.player.colliderect(monster.monster):
                    monster.monster[1] -= (1 *  monster.speed)
            if player.player[0] - monster.monster[0]  > 0 and not player.player.colliderect(monster.monster):
                    monster.monster[0] += (1 *  monster.speed)
            if player.player[0] - monster.monster[0]  < 0 and not player.player.colliderect(monster.monster) :
                    monster.monster[0] -= (1 *  monster.speed)
    
    def attack(self,player,window):
        for i,monster in enumerate(self.monster_list):
            if player.player.colliderect(self.monster_list[i].monster):
                if pygame.time.get_ticks() - monster.last_attack  >= monster.cd  :
                    dmg2 =  player.title.render("-" + str(monster.DMG) , True,player.color)
                    player.HP -= monster.DMG
                    print(player.HP)
                    player.display = True
                    monster.last_attack =  pygame.time.get_ticks()
                    
        
        if player.display == True:             
            window.blit(dmg2,(player.player[0] - 10,player.player[1] - 50))
            player.display = False
        