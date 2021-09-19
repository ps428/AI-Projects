import pygame
import piece
import values

class game_Board:
    def __init__(self):
        self.board = []
        self.player_count_black = 12
        self.player_count_white = 12
        self.kings_count_black = 0
        self.kings_count_white = 0

        
    def fill_block(window, row, column):
        # Fill a rectangle at row, column with height and width equal to BLOCK_SIZE
        pygame.draw.rect(window, values.LIGHT, (row*values.BLOCK_SIZE, column*values.BLOCK_SIZE, values.BLOCK_SIZE, values.BLOCK_SIZE))

    def draw_blocks(self, window):
        window.fill(values.DARK)
        for row in range(values.ROWS):
            for column in range(values.COLUMNS):
                # For even columns, fill even rows with light
                if column%2==0:
                    if row%2!=0:
                        # print("--------")
                        pygame.draw.rect(window, values.LIGHT, (row*values.BLOCK_SIZE, column*values.BLOCK_SIZE, values.BLOCK_SIZE, values.BLOCK_SIZE))
                else:
                    if row%2==0:
                        pygame.draw.rect(window, values.LIGHT, (row*values.BLOCK_SIZE, column*values.BLOCK_SIZE, values.BLOCK_SIZE, values.BLOCK_SIZE))
                        
                    
    def get_piece(self, x, y):
        return self.board[x][y]


