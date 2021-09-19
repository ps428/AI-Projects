import pygame
import game_values
import game_pieces

class game_Board:
    # 2d list with 8 rows and 8 columns
    def __init__(self):
        self.red_count = 12
        self.white_count = 12

        self.red_king = 0
        self.white_king = 0

        self.game_board = [] # Empty board
        
        self.piece_active = None # No active piece selected for now

        self.make_board()
        
    def make_game_cubes(self, window):
        window.fill(game_values.BLACK)

        for row in range(0,game_values.ROWS):
            for column in range((row+1)%2, game_values.ROWS, 2):
                # Draw squares of colour in window of at location (x, y, w, h) with height h and width w
                pygame.draw.rect(window, game_values.RED, (row*game_values.SQUARE_SIZE, column*game_values.SQUARE_SIZE, game_values.SQUARE_SIZE, game_values.SQUARE_SIZE))

        

    def move(self, piece, row, column):
        tmp = self.game_board[piece.row][piece.column]
        self.game_board[piece.row][piece.column] = self.game_board[row][column] 
        self.game_board[row][column] = tmp
        # self.game_board[piece.row][piece.column], self.game_board[row][column] = self.game_board[row][column], self.game_board[piece.row][piece.column]

        piece.move_piece(row, column)

        # Checking if the piece becomes the king
        if piece.row == game_values.ROWS -1 or piece.row == 0:
            piece.king = True
            if piece.color == game_values.WHITE:
                self.white_king+=1
            else:
                self.red_king+=1

    def get_piece(self, row, column):
        return self.game_board[row][column]

    def make_board(self):
        for row in range(0, game_values.ROWS):
            # What each row has inside it
            self.game_board.append([])
            for column in range(0,game_values.COLUMNS):
                if column%2==0:
                    if row%2==0:
                        if(row<=2):
                            self.game_board[row].append(game_pieces.game_Piece(row, column, game_values.WHITE))
                        elif row>=5:
                            self.game_board[row].append(game_pieces.game_Piece(row, column, game_values.RED))
                        else:
                            self.game_board[row].append(0)
                    else:
                        self.game_board[row].append(0)
                    

                elif column%2!=0:
                    if row%2!=0:
                        if(row<=2):
                            self.game_board[row].append(game_pieces.game_Piece(row, column, game_values.WHITE))
                        elif row>=5:
                            self.game_board[row].append(game_pieces.game_Piece(row, column, game_values.RED))
                        else:
                            self.game_board[row].append(0)
                    else:
                        self.game_board[row].append(0)
                
               

    def draw_all(self, window):
        self.make_game_cubes(window)


        for row in range(0, game_values.ROWS):
            for column in range(0, game_values.COLUMNS):
                curr_piece = self.game_board[row][column]
                if curr_piece!=0:
                    curr_piece.draw_piece(window)