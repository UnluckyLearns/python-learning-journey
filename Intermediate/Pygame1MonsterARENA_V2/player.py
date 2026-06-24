import pygame

class Player():
    def __init__(self):
        self.title = pygame.font.SysFont("Arial", 20)
        self.player = pygame.Rect(610,610,20,20)
        self.project = pygame.Rect(0,0,50,5)
        self.HP = 100
        self.DMG = 12
        self.display = False
        self.proj_display = False
        self.duration = 20
        self.movement = [False,False,False,False]
        self.speed = 8
        self.color = "yellow"

    def update_movement(self):
            self.player[1] += (self.movement[1] - self.movement[0]) * self.speed
            self.player[0] += (self.movement[2] - self.movement[3]) * self.speed
            self.player[1] = max(0,min(self.player[1],610))
            self.player[0] = max(0,min(self.player[0],610))
    
    def move(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                    self.project[1]= self.player[1] 
                    self.project[0] = self.player[0]
                    self.proj_display = True
            if event.key == pygame.K_UP:   self.movement[0] = True
            if event.key == pygame.K_DOWN: self.movement[1] = True
            if event.key == pygame.K_RIGHT:self.movement[2] = True
            if event.key == pygame.K_LEFT: self.movement[3] = True
        if event.type ==  pygame.KEYUP:
            if event.key == pygame.K_UP: self.movement[0] = False
            if event.key == pygame.K_DOWN: self.movement[1] = False
            if event.key == pygame.K_RIGHT: self.movement[2] = False
            if event.key == pygame.K_LEFT: self.movement[3] = False

