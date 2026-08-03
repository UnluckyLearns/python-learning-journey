import pygame
from settings import *
import sys

class Interface():
    def __init__(self):
        self.red = pygame.image.load(HEART_PATH).convert_alpha()
        self.quit = pygame.image.load(QUIT_PATH).convert_alpha()
        self.over = pygame.image.load(OVER_PATH).convert_alpha()
        self.retry = pygame.image.load(RETRY_PATH).convert_alpha()
        self.font = pygame.font.Font(FONT_PATH, 24)
        self.score = 0
        self.center_rect = self.over.get_rect(center=(400,400))
        self.left_rect  = self.retry.get_rect(center=(300,600))
        self.right_rect  = self.quit.get_rect(center=(500,600))


    def draw_hp(self,window,HP):
        for i in range(HP):
            window.blit(self.red,(i*43,0))

    def game_over(self,window):
        window.blit(self.over,self.center_rect)
        window.blit(self.retry,self.left_rect)
        window.blit(self.quit,self.right_rect)

        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            x,y = pygame.mouse.get_pos()
            if self.left_rect.collidepoint((x,y)):
                    return(1)
            if self.right_rect.collidepoint((x,y)):
                    pygame.quit()
                    sys.exit()

    def draw_score(self,window):
         text = self.font.render(f"score: {self.score}",True,"White")
         window.blit(text,(600,10))


