import pygame


class Pieces():
    def __init__(self,color,col ,row,piece_name):
        self.row = row
        self.col = col
        self.poss_moves = []
        self.color = color
        self.load = pygame.image.load(rf"C:\Users\User\Desktop\test\Chess\Chess_Pieces\{color}\{piece_name}.png")
    
    def get_pos(self,board):
        print("here2")
        self.poss_moves = []
        for r,c in self.direction:
            row = self.row + r
            col = self.col + c            
            while  0  <= row < 8 and 0  <= col < 8:
                    if board[col][row].piece:
                        if board[col][row].piece.color == board[self.col][self.row].piece.color:
                            break
                        else:
                            self.poss_moves.append((row,col))
                            break
                    self.poss_moves.append((row,col))
                    row += r
                    col += c
        return self.poss_moves

class Pawns(Pieces):
    def __init__(self, color,col ,row,):
        self.counter = 0
        super().__init__(color,col ,row,"Pawn")
    
    def get_pos(self, board):
        self.poss_moves = []
        if self.color == "White":
            if self.col + 1 <= 7:
                if self.row + 1 <= 7:
                    if board[self.col + 1][self.row + 1].piece:
                        if board[self.col + 1][self.row + 1].piece.color == "Black":
                            self.poss_moves.append((self.row + 1, self.col + 1))
                if self.row - 1 >= 0:
                    if board[self.col + 1][self.row - 1].piece:
                        if board[self.col + 1][self.row - 1].piece.color == "Black":
                            self.poss_moves.append((self.row - 1, self.col + 1))
                if not board[self.col + 1][self.row].piece:
                    self.poss_moves.append((self.row, self.col + 1))
                    if self.counter == 0:
                        self.counter = 1
                        if self.col + 2 <= 7:
                            if not board[self.col + 2][self.row].piece:
                                self.poss_moves.append((self.row, self.col + 2))
        elif self.color == "Black":
            if self.col - 1 >= 0:
                if self.row + 1 <= 7:
                    if board[self.col - 1][self.row + 1].piece:
                        if board[self.col - 1][self.row + 1].piece.color == "White":
                            self.poss_moves.append((self.row + 1, self.col - 1))
                if self.row - 1 >= 0:
                    if board[self.col - 1][self.row - 1].piece:
                        if board[self.col - 1][self.row - 1].piece.color == "White":
                            self.poss_moves.append((self.row - 1, self.col - 1))
                if not board[self.col - 1][self.row].piece:
                    self.poss_moves.append((self.row, self.col - 1))
                    if self.counter == 0:
                        self.counter = 1
                        if self.col - 2 >= 0:
                            if not board[self.col - 2][self.row].piece:
                                self.poss_moves.append((self.row, self.col - 2))
        return self.poss_moves

class Rook(Pieces):
    def __init__(self, color, col ,row):
        self.direction  = [(0,1),(0,-1),(1,0),(-1,0)]
        super().__init__(color, col ,row,"Rook")
    



class King(Pieces):
    def __init__(self, color, col ,row):
        self.direction = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
        super().__init__(color,col ,row,"King")
    def get_pos(self,board):
        self.poss_moves = []
        for r,c in self.direction:
            row = self.row + r
            col = self.col + c
            if 0  <= row < 8 and 0  <= col < 8:
                if board[col][row].piece and board[col][row].piece.color == board[self.col][self.row].piece.color:
                        continue
                else:
                    self.poss_moves.append((row,col))
        return self.poss_moves


class Queen(Pieces):
    def __init__(self, color, col ,row):
        self.direction  = [(1,1),(1,-1),(-1,1),(-1,-1),(0,1),(0,-1),(1,0),(-1,0)]
        super().__init__(color, col ,row,"Queen")


class Bishop(Pieces):
    def __init__(self, color, col ,row):
        self.direction  = [(1,1),(1,-1),(-1,1),(-1,-1)]
        super().__init__(color,col ,row,"Bishop")


class Knight(Pieces):
    def __init__(self, color, col ,row):
        self.direction  = [(2,1),(2,-1),(-2,1),(1,-2),(1,2),(-1,-2),(-1,2)]
        super().__init__(color, col ,row,"Knight")
    
    def get_pos(self,board):
        self.poss_moves = []
        for r,c in self.direction:
            row = self.row + r
            col = self.col + c
            if 0  <= row < 8 and 0  <= col < 8:
                if board[col][row].piece and board[col][row].piece.color == board[self.col][self.row].piece.color:
                        continue
                else:
                    self.poss_moves.append((row,col))
        return self.poss_moves


