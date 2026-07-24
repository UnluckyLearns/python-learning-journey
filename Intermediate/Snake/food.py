import pygame
import random

class Food():
    def __init__(self):
        self.pos = [random.randint(0,15),random.randint(0,15)]
        self.rect = ()


    def spawn_food(self,window):
        self.rect = pygame.draw.rect(window,"Purple",(self.pos[0]*50,self.pos[1]*50,50,50))
        return self.rect