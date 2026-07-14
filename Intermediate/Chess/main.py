import pygame
import sys
from squares import Square
from pieces import Rook,Bishop,Queen,King,Pawns,Knight

class Game():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800,800))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 60)
        self.board = []
        self.size = 100
        self.hightlight = "Yellow"
        self.hi =  []
        self.past = []
        self.poss_moves= []
        self.test = 0
        self.selected = []
        self.message = ""
        
        self.game_end = False
        pygame.display.set_caption("Small Chess Game")
    

    def draw_square(self,color,col,row):
        pygame.draw.rect(self.window,color,(col*100,row*100,self.size,self.size))
        pygame.draw.rect(self.window, "black", (col*100, row*100, self.size, self.size), width=3)
    
    def fix_pieces(self):
        white_pieces  = [Rook("White",0,0),Knight("White",0,1),Bishop("White",0,2),Queen("White",0,3),King("White",0,4),Bishop("White",0,5),Knight("White",0,6),Rook("White",0,7),Pawns("White",1,0),Pawns("White",1,1),Pawns("White",1,2),Pawns("White",1,3),Pawns("White",1,4),Pawns("White",1,5),Pawns("White",1,6),Pawns("White",1,7)]
        black_pieces = [Rook("Black",7,0),Knight("Black",7,1),Bishop("Black",7,2),Queen("Black",7,3),King("Black",7,4),Bishop("Black",7,5),Knight("Black",7,6),Rook("Black",7,7),Pawns("Black",6,0),Pawns("Black",6,1),Pawns("Black",6,2),Pawns("Black",6,3),Pawns("Black",6,4),Pawns("Black",6,5),Pawns("Black",6,6),Pawns("Black",6,7)]
        for row in range(8):
            self.board[0][row].piece = white_pieces[row]
            self.board[7][row].piece = black_pieces[row]
            self.board[1][row].piece = white_pieces[8+row]
            self.board[6][row].piece = black_pieces[8+row]
            self.window.blit(self.board[0][row].piece.load.convert_alpha(), ((row*100) + 25,(0) + 25))
            self.window.blit(self.board[7][row].piece.load.convert_alpha(), ((row*100) + 25,(700) + 25))
            self.window.blit(self.board[1][row].piece.load.convert_alpha(), ((row*100) + 25,(100) + 25))
            self.window.blit(self.board[6][row].piece.load.convert_alpha(), ((row*100) + 25,(600) + 25))
    
    def draw_board(self):
        for col in range(8):
            line = []
            for row in range(8):
                if (col + row) % 2 == 0 : color = "white"
                else: color = "red"
                rect = pygame.draw.rect(self.window,color,(col*100,row*100,self.size,self.size))
                line.append(Square(col,row,rect,color))
            self.board.append(line)
    
    def update_colors(self):
        if self.past:
            if self.past != self.poss_moves:
                for poses in self.past:
                    if (poses[0] + poses[1]) % 2 == 0 : 
                        self.board[poses[1]][poses[0]].color = "white"
                    else: self.board[poses[1]][poses[0]].color = "red"
            self.past = []
        if self.poss_moves:
            for poses in self.poss_moves:
                if self.board[poses[1]][poses[0]].piece :
                    self.board[poses[0]][poses[1]].color = "Green"
                else:
                    self.board[poses[0]][poses[1]].color = "Yellow"
                self.past.append((poses[1],poses[0]))
        

    def update_board(self):
        for col in range(8):
            for row in range(8):
                p_row = self.board[col][row].row
                p_col = self.board[col][row].col
                self.draw_square(self.board[col][row].color,p_col,p_row)
        if self.game_end:
            text_surface = self.font.render(self.message, True, "Purple")
            self.window.blit(text_surface, (50, 300))

    def update_pieces(self):
        for col in range(8):
            for row in range(8):
             if self.board[col][row].piece : 
                p_row = self.board[col][row].piece.row
                p_col = self.board[col][row].piece.col
                self.window.blit(self.board[col][row].piece.load.convert_alpha(), ((p_row*100) + 25,(p_col*100) + 25))

    def move(self,pos):
        if self.board[pos[1]//100][pos[0]//100].piece:
                if isinstance(self.board[pos[1]//100][pos[0]//100].piece,King):
                    self.message = self.board[pos[1]//100][pos[0]//100].piece.color + "  LOST   " + self.board[self.selected[0]][self.selected[1]].piece.color + "  WON   "
                    self.game_end = True
                self.board[pos[1]//100][pos[0]//100].piece  = self.board[self.selected[0]][self.selected[1]].piece
                self.board[pos[1]//100][pos[0]//100].piece.col =  self.board[pos[1]//100][pos[0]//100].col
                self.board[pos[1]//100][pos[0]//100].piece.row =  self.board[pos[1]//100][pos[0]//100].row
                self.board[self.selected[0]][self.selected[1]].piece = None
                self.selected = (self.board[pos[1]//100][pos[0]//100])
        else:
            self.board[self.selected[0]][self.selected[1]].piece.col = self.board[pos[1]//100][pos[0]//100].col
            self.board[self.selected[0]][self.selected[1]].piece.row = self.board[pos[1]//100][pos[0]//100].row
            self.board[pos[1]//100][pos[0]//100].piece = self.board[self.selected[0]][self.selected[1]].piece
            self.board[self.selected[0]][self.selected[1]].piece = None
        self.poss_moves = []



    def new_game(self):
        self.draw_board()
        self.fix_pieces()
        turn = "White"
        while True:
            self.update_colors()
            self.update_board()
            self.update_pieces()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                    c_row = event.pos[0]//100
                    c_col = event.pos[1]//100
                    if self.board[c_col][c_row].piece and self.board[c_col][c_row].piece.color == turn :                        
                        if (c_row,c_col) in self.poss_moves: 
                            if turn == "White":
                                turn = "Black"
                            else:
                                turn = "White"
                        else:
                            self.poss_moves = self.board[c_col][c_row].piece.get_pos(self.board)   
                            self.selected = (c_col,c_row)
                    else : 
                        if (event.pos[0]//100,event.pos[1]//100) in self.poss_moves:
                            self.move(event.pos)
                            if turn == "White":
                                turn = "Black"
                            else:
                                turn = "White"
           
            pygame.display.flip()
            self.clock.tick(60)        

def main():
    Game().new_game()


if __name__ == "__main__":
    main()