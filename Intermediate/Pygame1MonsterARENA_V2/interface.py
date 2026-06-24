import pygame

class Interface():
    def __init__(self):
        self.number = 0
        self.HP = 0
        self.wave_num = 0
    

    def display_ui(self,player,window,monster):
        self.HP = player.HP
        self.wave_num = monster.wave
        self.number = len(monster.monster_list)
        text = pygame.font.SysFont("arial",30)
        ui = text.render("HP : " + str(self.HP) + "\n" + "ENEMIES : " + str(self.number) + "\n" + "WAVE : " + str(self.wave_num),True,"red")
        window.blit(ui,(0,0))
    

    def display_over(self,window):
        text = pygame.font.SysFont("arial",60)
        ui = text.render(" GAME OVER"+ "\n" + "Press R to Retry"+ "\n" + "Press Q to Quit" ,True,"black")
        window.blit(ui,(150,200))
