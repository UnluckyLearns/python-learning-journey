import pygame
import random
from settings import *

class Block():
    def __init__(self,posX,posY):
        self.poss_x =[0,36,72,108, 144]
        self.poss_y = [0,20,40]
        self.block = pygame.image.load(BLOCK1_PATH).convert_alpha()
        self.rect = self.block.get_rect()
        self.rect.inflate_ip(-5,0)
        self.hp = random.randint(1,2)
        self.posX = posX
        self.posY = posY 


    def print_block(self,window):
        if self.hp == 1:
            window.blit(self.block,self.rect)
        if self.hp == 2:
            self.block = pygame.image.load(BLOCK2_PATH).convert_alpha()
            window.blit(self.block,self.rect)


    def update_rect(self):
        self.rect.x = self.posX
        self.rect.y= self.posY
            

