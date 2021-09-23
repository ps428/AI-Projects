import pygame
import values
import board

class playGame:
    def __init__(self, window):
        self.active_piece = None
        self.board = board.game_Board()
        self.chance = values.BLUE
        self.window = window

    def update(self):
        self.board.current_status(self.window)
        pygame.display.update()
    
    def reset(self):
        self.active_piece = None
        self.board = board.game_Board()
        self.chance = values.BLUE
        self.update()
    
    def select_or_move(self, x,y):
        if self.active_piece==None or self.active_piece==0:
            print("vacant",self.active_piece)
            self.active_piece = self.board.get_piece(x,y)
        else:
            print("piece",self.active_piece.row, self.active_piece.column)
            self.make_move(x,y)
        self.update()

    def make_move(self, x, y):
        # print("from:",self.active_piece.row,self.active_piece.column)
        # print("to:",x,y)
        self.board.make_move(self.active_piece, x, y)
        # self.active_piece.move(x,y)
        self.active_piece = None

    def change_chance(self):
        if self.chance == values.RED:
            self.chance = values.BLUE
        else:
            self.chance = values.BLUE