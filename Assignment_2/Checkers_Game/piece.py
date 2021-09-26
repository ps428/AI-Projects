import pygame
import values

class Piece:
    def __init__(self, row, column, color):
        self.king = False # initially not a king
        # Location of piece in the board
        self.x = 0
        self.y = 0

        self.row = row
        self.column = column
        
        self.get_position()
        self.color = color
        
    def get_position(self):
        self.x = self.column*values.BLOCK_SIZE + values.BLOCK_SIZE//2
        self.y = self.row*values.BLOCK_SIZE + values.BLOCK_SIZE//2

    def draw_piece(self, window):
        size = values.BLOCK_SIZE//6
        pygame.draw.circle(window, values.BLACK, (self.x, self.y), size + values.BLOCK_SIZE//20)
        pygame.draw.circle(window, self.color, (self.x, self.y), size)
        if self.king:
            pygame.draw.circle(window, values.KING, (self.x, self.y), size - values.BLOCK_SIZE//12)

    def move(self,row,column):
        self.row = row
        self.column = column
        self.get_position()
