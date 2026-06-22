import pygame

class Monster():
    def __init__(self):
        self.title = pygame.font.SysFont("arial",20)
        self.monster = pygame.Rect(50,100,20,20)
        self.HP = 80
        self.DMG = 10
        self.display = False
        self.duration = 20
        self.cd = 2000
    
    def chase(self,player):
        if player.player[1] - self.monster[1]  > 0 :
            self.monster[1] += 1
        if player.player[1] - self.monster[1]  < 0 :
            self.monster[1] -= 1
        if player.player[0] - self.monster[0]  > 0 :
            self.monster[0] += 1
        if player.player[0] - self.monster[0]  < 0 :
            self.monster[0] -= 1
    
    def attack(self,player,current):
        if current  + self.cd <  pygame.time.get_ticks():
            player.HP -= self.DMG
            player.display = True
            player.duration = 20
            current = pygame.time.get_ticks()
            print(player.HP)
        return current   
