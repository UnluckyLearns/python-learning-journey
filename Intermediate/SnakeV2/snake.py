import pygame

class Snake():
    def __init__(self):
        self.direction = "Up"
        self.move_dict = { "Up": (0,-1),"Down": (0,1),"Right" : (1,0) ,"Left" : (-1,0)}
        self.head =[8,8]
        self.rect = ()
        self.body = [[8,9],[8,10]]
        self.dead = False
        self.grow = False

    
    def draw_snake(self,window):
        for pos in self.body:
            pygame.draw.rect(window,"Yellow",(pos[0]*50,pos[1]*50,50,50))
        self.rect = pygame.draw.rect(window,"black",(self.head[0]*50,self.head[1]*50,50,50))

    
    def move_snake(self):
        old_head = self.head.copy()
        self.body.insert(0,old_head)
        if not self.grow:
            self.body.pop()
        else : 
            self.grow = False
        self.head[0] =  self.head[0] + self.move_dict[self.direction][0]
        self.head[1] =  self.head[1] + self.move_dict[self.direction][1]
        if self.head[0] > 15 or self.head[1] > 15 or self.head[0]  < 0 or self.head[1] < 0 :
            self.dead = True
            return

