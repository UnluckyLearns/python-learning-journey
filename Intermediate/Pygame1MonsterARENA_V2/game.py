import pygame
import sys
from  player import Player
from monster import Monster
from monster_manager import MonsterManager
import time
from interface import Interface

class Game():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((640,640))
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.monster = Monster()
        self.monst = MonsterManager()
        self.flag = 1
        self.opp1 = self.monst.spawn_monster()
        self.ui = Interface()
        pygame.display.set_caption("MINI ARENA GAME")

    
    def restart_game(self):
        self.player = Player()
        self.monst = MonsterManager()
        self.opp1 = self.monst.spawn_monster()
        self.flag = 1
    
    def run_game(self):
        while True:
            self.window.fill((14,219,248))
            if self.flag == 1:
                self.ui.display_ui(self.player,self.window,self.monst)
                color1="yellow"
                self.player.update_movement()
                self.monst.move_monster(self.player)
                name1 = self.player.title.render("PLAYER1",True,color1)
                self.window.blit(name1,(self.player.player[0] - 30,self.player.player[1] - 25))
                pygame.draw.rect(self.window,color1,self.player.player)
                for items in self.opp1:
                    name = items.title.render(items.name, True, items.color)
                    self.window.blit(name, (items.monster[0] - 30, items.monster[1] - 30))
                    pygame.draw.rect(self.window,items.color,items.monster)
                

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    self.player.move(event)

                if self.player.proj_display == True : 
                    pygame.draw.rect(self.window,color1,self.player.project)
                    for i,opp in enumerate(self.opp1): 
                        if self.player.project.colliderect(opp.monster):
                                dmg =  self.player.title.render("-" + str(self.player.DMG),True,opp.color)
                                self.window.blit(dmg,(opp.monster[0] - 10,opp.monster[1] - 50))
                                opp.HP -= self.player.DMG
                                if opp.HP <= 0 :
                                    del self.opp1[i]
                                else:
                                    opp.duration = 20
                                    opp.display = True
                                self.player.proj_display = False
                    self.player.project[0] += 30
                    if self.player.project[0]  > 640:
                        self.player.proj_display = False
                self.player.duration -= 1

                self.monst.attack(self.player,self.window)

                

                if not self.opp1:
                    self.monst.wave += 1
                    self.opp1 = self.monst.spawn_monster()


                if self.player.HP  <= 0:
                    self.flag = 0
            
            else:
                self.ui.display_over(self.window)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            self.restart_game()
                        if event.key == pygame.K_q:
                            pygame.quit()
                            sys.exit()
            pygame.display.update()
            self.clock.tick(60)

def main():
    Game().run_game()


if __name__ == "__main__":
    main()