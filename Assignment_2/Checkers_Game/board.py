from typing import Collection
import pygame
import piece
import values

class game_Board:
    def __init__(self):
        self.board = []
        self.player_count_dark = 12
        self.player_count_light = 12
        self.kings_count_dark = 0
        self.kings_count_light = 0
        self.make_pieces()
        
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
      
        for row in range(values.ROWS):
            for column in range(values.COLUMNS):
                if self.board[row][column] != 0:
                    self.board[row][column].draw_piece(window)
                        
    def make_pieces(self):
        for row in range(0, values.ROWS):
            self.board.append([])
            for column in range(0, values.COLUMNS):
                if column%2==0:
                    if row%2!=0 and row<=2:
                        self.board[row].append(piece.Piece(row, column, values.BLUE))
                    elif row%2!=0 and row>=5:
                        self.board[row].append(piece.Piece(row, column, values.RED))
                    else:
                        self.board[row].append(0)
                
                if column%2!=0:
                    if row%2==0 and row<=2:
                        self.board[row].append(piece.Piece(row, column, values.BLUE))
                    elif row%2==0 and row>=5:
                        self.board[row].append(piece.Piece(row, column, values.RED))
                    else:
                        self.board[row].append(0)
                

    def get_piece(self, x, y):
        return self.board[x][y]

    def get_all_pieces_colorwise(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece.color == color:
                    pieces.append(piece)
        
        return pieces

    def make_move(self, piece, x, y):
        # make a change (swap) in the board matrix
        tmp = self.board[piece.row][piece.column]
        self.board[piece.row][piece.column] = self.board[x][y]
        self.board[x][y] = tmp

        # execute the move on the piece
        piece.move(x,y)

        # Dealing with kings
        if x == 0 or x == values.ROWS-1:
            piece.make_king()

        if piece.color == values.LIGHT:
            self.kings_count_light+=1
        else:
            self.kings_count_dark+=1

