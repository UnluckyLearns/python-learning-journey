import pygame
from settings import *
vec = pygame.math.Vector2

class Balls():
    def __init__(self):
        self.ball = pygame.image.load(BALL_PATH).convert_alpha()
        self.pos = vec(WIDTH/2,HEIGHT/2)
        self.velo = vec(0,7)
        self.rect = self.ball.get_rect()
        self.hori = 0
        self.vert = 0


    def draw_ball(self,window):
        window.blit(self.ball,self.rect)

        
    def check_collision_paddle(self,paddle):
        if self.rect.colliderect(paddle.rect["Left"]):
            self.velo = vec(-1, -8)
        elif self.rect.colliderect(paddle.rect["Mid"]):
            self.velo = vec(0,-8)
        elif self.rect.colliderect(paddle.rect["Right"]):
            self.velo = vec(1, -8)

    def check_collision_blocks(self,blocks,interface):
        temp = None
        for block in blocks.level:
            if self.rect.colliderect(block.rect):
                left   = self.rect.right - block.rect.left
                right  = block.rect.right - self.rect.left
                top    = self.rect.bottom - block.rect.top
                bottom = block.rect.bottom - self.rect.top
                horizontal = min(left, right)
                vertical = min(top, bottom)
                temp  = block 
                break
        if temp:
            temp.hp -= 1
            if temp.hp  <= 0:
                blocks.level.remove(temp)
                interface.score+=1
            if horizontal < vertical:
                self.velo = self.velo.reflect((-1,0))
            else:
                self.velo = self.velo.reflect((0,-1))



    def move_ball(self,paddle,blocks,interface):
        self.pos += self.velo
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        if self.pos.y   < EDGE_MIN:
            self.velo = self.velo.reflect((0, 1))
        if self.pos.y   > EDGE_MAX:
            paddle.hp -= 1
            self.pos = vec(WIDTH/2,HEIGHT/2)
            self.velo = vec(0,2)
        if self.pos.x < EDGE_MIN :
            self.velo = self.velo.reflect((1, 0))
        if self.pos.x > EDGE_MAX:
            self.velo = self.velo.reflect((-1, 0))       
        self.check_collision_paddle(paddle)
        self.check_collision_blocks(blocks,interface)

        