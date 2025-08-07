import game_values
import pygame

class game_Piece:
    def __init__(self, row, column, color):
        self.row = row
        self.column = column
        self.color = color
        if color==game_values.WHITE:
            self.color2 = game_values.RED
        else:
            self.color2 = game_values.WHITE
        self.king = False
        self.piece_active = False
        
        if self.color == game_values.RED:
            self.direction = 1
        else:
            self.direction = -1
        
        self.x = 0
        self.y = 0

        self.get_position()

    # To get positions
    def get_position(self):
        self.x = game_values.SQUARE_SIZE*self.column + game_values.SQUARE_SIZE//2
        self.y = game_values.SQUARE_SIZE*self.row + game_values.SQUARE_SIZE//2

    def change_to_king(self):
        self.king = True
    
    def draw_piece(self, window):
        radius = game_values.SQUARE_SIZE//4
        pygame.draw.circle(window, self.color2, (self.x,self.y), radius + game_values.SQUARE_SIZE//25)
        pygame.draw.circle(window, self.color, (self.x, self.y),radius)

        # Golden colout for king
        if self.king:
            pygame.draw.circle(window, game_values.GOLDEN, (self.x, self.y),radius//2)

    def move_piece(self, x, y):
        self.row = x
        self.column = y
        self.get_position()
# def __refr__