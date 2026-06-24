import pygame
import random
class Monster():
    def __init__(self):
        self.name = ""
        self.title = pygame.font.SysFont("arial",20)
        self.monster = pygame.Rect(random.randint(0,300),random.randint(0,400),20,20)
        self.color = ""
        self.HP = 80
        self.DMG = 10
        self.display = False
        self.duration = 20
        self.cd = 2000
        self.speed = 0
        self.last_attack = 0
    

