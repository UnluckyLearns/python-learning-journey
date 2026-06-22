import pygame
import sys
from  player import Player
from monster import Monster
import time

class Game():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((640,640))
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.monster = Monster()
        pygame.display.set_caption("Test Screen ")
    
    def run_game(self):
        
        current = pygame.time.get_ticks()
        while True:
            self.window.fill((14,219,248))
            color1="green"
            color2="red"
            self.player.update_movement()
            if self.player.player.colliderect(self.monster.monster):
                current= self.monster.attack(self.player,current)
                color1="white"
                color2="black"
                pygame.draw.rect(self.window,color2,self.monster.monster)
                pygame.draw.rect(self.window,color1,self.player.player)
            else: 
                self.monster.chase(self.player)
            name1 = self.player.title.render("PLAYER1",True,color1)
            name2 = self.monster.title.render("MONSTER1",True,color2)
            dmg1 =  self.player.title.render("-" + str(self.player.DMG),True,color2)
            dmg2 =  self.player.title.render("-" + str(self.monster.DMG),True,color1)
            self.window.blit(name2,(self.monster.monster[0] - 40,self.monster.monster[1] - 25))
            self.window.blit(name1,(self.player.player[0] - 30,self.player.player[1] - 25))

            pygame.draw.rect(self.window,color2,self.monster.monster)
            pygame.draw.rect(self.window,color1,self.player.player)
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.player.move(event,self.monster)

            self.monster.duration -= 1
            self.player.duration -= 1
            if self.player.display == True:
                self.window.blit(dmg2,(self.player.player[0] - 10,self.player.player[1] - 50))
            if self.player.duration  == 0:
                self.player.display = False
            if self.monster.display == True:
                self.window.blit(dmg1,(self.monster.monster[0] - 10,self.monster.monster[1] - 50))
            if self.monster.duration  == 0:
                self.monster.display = False
            
            if self.monster.HP  <= 0:
                print("Game Won")
                pygame.quit()
                sys.exit()

            if self.player.HP  <= 0:
                print("Game LOST")
                pygame.quit()
                sys.exit()
            
            pygame.display.update()
            self.clock.tick(60)

def main():
    Game().run_game()


if __name__ == "__main__":
    main()