import pygame
import sys
from snake import Snake
from food import Food

class Game():
    def __init__(self):
        self.counter = 0
        self.snake = Snake()
        pygame.init()
        self.window = pygame.display.set_mode((800,800))
        self.clock = pygame.time.Clock()
        self.grid =  []
        self.food = Food()
        pygame.display.set_caption = "Mini Snake Game"
    
    def draw_square(self,col,row):
        rect = pygame.draw.rect(self.window,"White",(col*50,row*50,50,50))
        pygame.draw.rect(self.window,"Black",(col*50,row*50,50,50),width=3)
        return rect


    def check_coli(self):
        if not self.snake.rect and self.food.rect:
            return
        if self.snake.rect.colliderect(self.food.rect):
            self.snake.add_node(self.food.pos)
            self.food = Food()


    def draw_grid(self):
        for col in range(16):
            line =  []
            for row in range(16):
               line.append(self.draw_square(col,row))
            self.grid.append(line)


    def display(self):
        while True:
            if self.snake.dead:
                pygame.quit()
                sys.exit()
            self.counter += 1
            if self.counter % 7 == 0:
                self.draw_grid()
                self.food.spawn_food(self.window)
                self.snake.move_snake()
                self.snake.draw_snake(self.window)
                self.check_coli()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if self.snake.direction != "Right":
                        if event.key == pygame.K_LEFT:
                            self.snake.direction = "Left"
                    if self.snake.direction != "Left":        
                        if event.key == pygame.K_RIGHT:
                            self.snake.direction = "Right"
                    if self.snake.direction != "Down":
                        if event.key == pygame.K_UP:
                            self.snake.direction = "Up"
                    if self.snake.direction != "Up":
                        if event.key == pygame.K_DOWN:
                            self.snake.direction = "Down"
                    

            pygame.display.flip()
            self.clock.tick(60)


def main():
    Game().display()


if __name__ == "__main__":
    main()