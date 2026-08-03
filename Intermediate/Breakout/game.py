import pygame
import sys
from player import Paddles
from ball import Balls
from settings import *
from level import Level
from interface import Interface

class Game():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()
        self.paddle = Paddles()
        self.ball = Balls()
        self.level = Level()
        self.interface = Interface()
        self.bg = pygame.image.load(BACKGROUND_PATH).convert_alpha()
        self.center = self.bg.get_rect(center=self.window.get_rect().center)
        pygame.display.set_caption("Mini Breakout")


    def  reset_game(self):
        self.paddle = Paddles()
        self.ball = Balls()
        self.level = Level()
        self.interface = Interface()
        self.level.generate_level()

    def new_game(self):
        self.level.generate_level()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.window.fill((0,0,0))
            self.window.blit(self.bg,self.center)
            self.level.draw_level(self.window)
            self.paddle.draw_paddle(self.window)
            self.ball.draw_ball(self.window)
            if self.paddle.hp <=  0:
                if self.interface.game_over(self.window):
                    self.reset_game()
            else:
                self.paddle.move()
                self.ball.move_ball(self.paddle,self.level,self.interface)
                self.interface.draw_score(self.window)

            self.interface.draw_hp(self.window,self.paddle.hp)
            if not self.level.level:
                self.level.lvl += 1
                self.level.generate_level()
            pygame.display.flip()
            self.clock.tick(60)


