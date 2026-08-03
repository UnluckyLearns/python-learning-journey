import pygame
import random
from block import Block
from settings import *

class Level():
    def __init__(self):
        self.level = []
        self.posX = LEVEL_STARTING_X
        self.posY = LEVEL_STARTING_Y
        self.lvl = 1

    def generate_level(self):
        self.posX = LEVEL_STARTING_X
        self.posY = LEVEL_STARTING_Y
        self.level = []
        for i in range(BLOCK_PER_LEVEL*self.lvl):
            self.level.append(Block(self.posX,self.posY))
            self.level[i].update_rect()
            self.posX += 30
            if (i+1) % 15 == 0:
                self.posY +=30
                self.posX =LEVEL_STARTING_X



    def draw_level(self,window):
        for blocks in self.level:
            blocks.print_block(window)