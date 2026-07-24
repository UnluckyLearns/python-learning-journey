import pygame

class Snake():
    def __init__(self):
        self.direction = "Down"
        self.move_dict = { "Up": (0,-1),"Down": (0,1),"Right" : (1,0) ,"Left" : (-1,0)}
        self.headyy =[8,8]
        self.rect = ()
        self.body = [[8,9],[8,10]]
        self.dead = False

    
    def draw_snake(self,window):
        for pos in self.body:
            pygame.draw.rect(window,"Yellow",(pos[0]*50,pos[1]*50,50,50))
        self.rect = pygame.draw.rect(window,"black",(self.headyy[0]*50,self.headyy[1]*50,50,50))

    
    def move_snake(self):
        if self.headyy[0] > 15 or self.headyy[1] > 15 or self.headyy[0]  < 0 or self.headyy[1] < 0 :
            self.dead = True
            return
        old_head = self.headyy.copy()
        self.body.insert(0,old_head)
        del  self.body[-1]
        self.headyy[0] =  self.headyy[0] + self.move_dict[self.direction][0]
        self.headyy[1] =  self.headyy[1] + self.move_dict[self.direction][1]

    def add_node(self,pos):
        old_head = self.headyy.copy()
        self.body.insert(0,old_head)
        self.headyy[0] =  pos[0]
        self.headyy[1] =  pos[1]


