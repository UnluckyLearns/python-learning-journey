import pygame

class Player():
    def __init__(self):
        self.title = pygame.font.SysFont("Arial", 20)
        self.player = pygame.Rect(0,0,20,20)
        self.HP = 100
        self.DMG = 12
        self.display = False
        self.duration = 20
        self.movement = [False,False,False,False]

    def update_movement(self):
        self.player[1] += (self.movement[1] - self.movement[0]) * 4
        self.player[0] += (self.movement[2] - self.movement[3]) * 4
        
    def move(self,event,monster):
        if event.type == pygame.KEYDOWN:
            if self.player.colliderect(monster.monster):
                if event.key == pygame.K_SPACE:
                    monster.HP-= self.DMG
                    monster.duration = 20
                    monster.display = True
            if event.key == pygame.K_UP:   self.movement[0] = True
            if event.key == pygame.K_DOWN: self.movement[1] = True
            if event.key == pygame.K_RIGHT:self.movement[2] = True
            if event.key == pygame.K_LEFT: self.movement[3] = True
        if event.type ==  pygame.KEYUP:
            if event.key == pygame.K_UP: self.movement[0] = False
            if event.key == pygame.K_DOWN: self.movement[1] = False
            if event.key == pygame.K_RIGHT: self.movement[2] = False
            if event.key == pygame.K_LEFT: self.movement[3] = False

