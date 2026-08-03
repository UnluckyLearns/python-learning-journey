import pygame
from settings import *
vec = pygame.math.Vector2
class Paddles():
    def __init__(self):
        self.sheet = pygame.image.load(PADDLE_PATH).convert_alpha()
        self.paddles =  {"Left" : self.sheet.subsurface((0, 0, PADDLE_THIRD_WIDTH, 25)),
                         "Mid"  : self.sheet.subsurface((PADDLE_THIRD_WIDTH, 0, PADDLE_THIRD_WIDTH, 25)),
                         "Right"  : self.sheet.subsurface((PADDLE_THIRD_WIDTH*2, 0, PADDLE_THIRD_WIDTH, 25)),}
        self.hp = PLAYER_HP
        self.pos = vec(400,600)
        self.velo = vec(0,0)
        self.accel = vec(0,0)
        self.fric = vec(0,0)
        self.rect = {"Left" : self.paddles["Left"].get_rect(),
                     "Mid" : self.paddles["Mid"].get_rect(),
                     "Right" : self.paddles["Right"].get_rect()}

    def draw_paddle(self,window):
        window.blit(self.paddles["Mid"],(self.pos.x,self.pos.y))
        window.blit(self.paddles["Left"],(self.pos.x-PADDLE_THIRD_WIDTH,self.pos.y))
        window.blit(self.paddles["Right"],(self.pos.x+PADDLE_THIRD_WIDTH,self.pos.y))
        pygame.draw.rect(window,"Green",self.rect["Mid"])
        pygame.draw.rect(window,"Blue",self.rect["Left"])
        pygame.draw.rect(window,"Yellow",self.rect["Right"])


    def update_rects(self):
        self.rect["Left"].x  = self.pos.x - PADDLE_THIRD_WIDTH
        self.rect["Left"].y  = self.pos.y
        self.rect["Left"].update(self.rect["Left"].x,self.rect["Left"].y,PADDLE_THIRD_WIDTH,1)

        self.rect["Mid"].x  = self.pos.x 
        self.rect["Mid"].y  = self.pos.y
        self.rect["Mid"].update(self.rect["Mid"].x,self.rect["Mid"].y,PADDLE_THIRD_WIDTH,1)

        self.rect["Right"].x  = self.pos.x + PADDLE_THIRD_WIDTH
        self.rect["Right"].y  = self.pos.y
        self.rect["Right"].update(self.rect["Right"].x,self.rect["Right"].y,PADDLE_THIRD_WIDTH,1)

    def move(self):
        self.accel = vec(0,0)
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] :
            self.accel.x = -PLAYER_ACC
        elif key[pygame.K_RIGHT]:
            self.accel.x = PLAYER_ACC
        self.accel += self.velo * PLAYER_FRICTION
        self.velo += self.accel
        
        self.pos += self.velo + PLAYER_ACC * self.accel
        if self.pos.x > WIDTH - PADDLE_HALF_WIDTH:
            self.pos.x = WIDTH -  PADDLE_HALF_WIDTH
        if self.pos.x  < PADDLE_HALF_WIDTH:
            self.pos.x =  PADDLE_HALF_WIDTH
        self.update_rects()
