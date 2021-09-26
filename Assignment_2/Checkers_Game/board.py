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
        pygame.draw.rect(window, values.OPTIONS_PANEL, (values.BLOCK_SIZE*values.ROWS, 0, values.OPTIONS_PANEL_SIZE+10, values.ROWS*values.BLOCK_SIZE +10))
        
        #Buttons
        # Random Game
        x = values.BLOCK_SIZE*values.ROWS + 2*values.OPTIONS_PANEL_SIZE//10
        y = values.ROWS//3*values.BLOCK_SIZE
        pygame.draw.rect(window, values.BUTTON_COLOR, (x, y, values.BLOCK_SIZE*2, values.BLOCK_SIZE//2))
        pygame.init()
        font = pygame.font.SysFont(None, 32)
        img1 = font.render('Random Game', True, values.BLUE)
        window.blit(img1, (x+10,y+10))


        # Min Max Game
        x = values.BLOCK_SIZE*values.ROWS + 2*values.OPTIONS_PANEL_SIZE//10
        y = 1.5*(values.ROWS//3*values.BLOCK_SIZE)
        pygame.draw.rect(window, values.LIGHT, (x, y, values.BLOCK_SIZE*2, values.BLOCK_SIZE//2))
        img1 = font.render('MinMax', True, values.BLUE)
        window.blit(img1, (x+45,y+10))
        
        # Alpha Beta Pruning 
        x = values.BLOCK_SIZE*values.ROWS + 2*values.OPTIONS_PANEL_SIZE//10
        y = 2*(values.ROWS//3*values.BLOCK_SIZE)
        pygame.draw.rect(window, values.LIGHT, (x, y, values.BLOCK_SIZE*2, values.BLOCK_SIZE//2))
        img1 = font.render('Alpha Beta', True, values.BLUE)
        window.blit(img1, (x+25,y+10))

        # Restart
        x = values.BLOCK_SIZE*values.ROWS + 2*values.OPTIONS_PANEL_SIZE//10
        y = 2.5*(values.ROWS//3*values.BLOCK_SIZE)
        pygame.draw.rect(window, values.LIGHT, (x, y, values.BLOCK_SIZE*2, values.BLOCK_SIZE//2))
        img1 = font.render('Restart Game', True, values.BLUE)
        window.blit(img1, (x+20,y+10))

        # Quit
        x = values.BLOCK_SIZE*values.ROWS + 2*values.OPTIONS_PANEL_SIZE//10
        y = 3*(values.ROWS//3*values.BLOCK_SIZE)
        pygame.draw.rect(window, values.LIGHT, (x, y, values.BLOCK_SIZE*2, values.BLOCK_SIZE//2))
        img1 = font.render('Quit Game', True, values.BLUE)
        window.blit(img1, (x+30,y+10))

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
      
        
                        
    def make_pieces(self):
        for row in range(0, values.ROWS):
            self.board.append([])#[[....],[....]]
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
                if piece!=0:
                    if piece.color == color:
                        pieces.append(piece)
        
        return pieces

    def make_move(self, piece, x, y):
        # make a change (swap) in the board matrix
        # change 1 board = [0,p1,0,p2,0,p3,0,p4]=>[0,p1,0,p2,0,p3,p4,0]
        # change 2 p4(0,7) => p4(0,6)
        # a,b=b,a
        self.board[piece.row][piece.column], self.board[x][y] = self.board[x][y],self.board[piece.row][piece.column]
        # z,b = b,z
        # tmp = self.board[piece.row][piece.column]
        # self.board[piece.row][piece.column] = self.board[x][y]
        # self.board[x][y] = tmp

        # change 2 p4(0,7) => p4(0,6)
        # execute the move on the piece
        piece.move(x,y)

        # Dealing with kings
        if x == 0 or x == values.ROWS-1:
            piece.king = True

            if piece.color == values.LIGHT:
                self.kings_count_light+=1
            else:
                self.kings_count_dark+=1
        

    def current_status(self, window):
        self.draw_blocks(window)
        for row in range(0, values.ROWS):
            for column in range(0, values.COLUMNS):
                piece = self.board[row][column]
                if piece != 0:
                    piece.draw_piece(window)

# TODO OUT OF MIND
    def get_possible_moves(self, curr_piece, moves_possible):
       
        if curr_piece.king == False:
            stance = True #Positive or negative movements allowed, True => Forward, positive movements
            x = curr_piece.row
            y = curr_piece.column
            x_p = x+1
            y_p = y+1
            x_n = x-1
            y_n = y-1

            
            if curr_piece.color == values.BLUE:
                stance =True
                # if forward elements are non zero, get possible moves
                if(x_p<=7 and y_p<=7):
                    if(self.board[x_p][y_p]==0):
                        moves_possible.append([x_p,y_p])
                    else:
                        filled_piece = self.board[x_p, y_p]
                        is_right = True
                        self._move_positive(piece, moves_possible, filled_piece, is_right)  

                if(x_n>=0 and y_p<=7):
                    if(self.board[x_n][y_p]==0):
                        moves_possible.append([x_n,y_p])
                    else:
                        filled_piece = self.board[x_n, y_p]
                        is_right = False
                        self._move_positive(piece, moves_possible, filled_piece, is_right)  

            else:
                stance = False    
                if(x_p<=7 and y_n>=0):
                    if(self.board[x_p][y_n]==0):
                        moves_possible.append([x_p,y_n])
                    else:
                        filled_piece = self.board[x_p, y_n]
                        is_right = True
                        self._move_negative(piece, moves_possible, filled_piece, is_right)  

                if(x_n>=0 and y_n>=0):
                    if(self.board[x_n][y_n]==0):
                        moves_possible.append([x_n,y_n])
                    else:
                        filled_piece = self.board[x_n, y_n]
                        is_right = False
                        self._move_negative(piece, moves_possible, filled_piece, is_right)  
        
        # King case
        else: 
            pass

    # Making these private, can be accessed only by class, not open to user
    def _move_positive(self, curr_piece, moves_possible, filled_piece, is_right):
        if(curr_piece.color != filled_piece.color):
            if(is_right):
                x_conquer = filled_piece.row + 1
                y_conquer = filled_piece.column + 1
                if(x_conquer<=7 and y_conquer<=7):
                    if(self.board[x_conquer][y_conquer]==0):
                        moves_possible.append([x_conquer,y_conquer])
                        new_piece  = piece.Piece(x_conquer, y_conquer, curr_piece.color)
                        self.get_possible_moves(new_piece,moves_possible)
           
            else:
                x_conquer = filled_piece.row - 1
                y_conquer = filled_piece.column + 1
                if(x_conquer>=0 and y_conquer<=7):
                    if(self.board[x_conquer][y_conquer]==0):
                        moves_possible.append([x_conquer,y_conquer])
                        new_piece  = piece.Piece(x_conquer, y_conquer, curr_piece.color)
                        self.get_possible_moves(new_piece,moves_possible)
        
    def _move_negative(self, curr_piece, moves_possible, filled_piece, is_right):
        if(curr_piece.color != filled_piece.color):
            if(is_right):
                x_conquer = filled_piece.row + 1
                y_conquer = filled_piece.column - 1
                if(x_conquer<=7 and y_conquer>=0):
                    if(self.board[x_conquer][y_conquer]==0):
                        moves_possible.append([x_conquer,y_conquer])
                        new_piece  = piece.Piece(x_conquer, y_conquer, curr_piece.color)
                        self.get_possible_moves(new_piece,moves_possible)
            else:
                x_conquer = filled_piece.row - 1
                y_conquer = filled_piece.column - 1
                if(x_conquer>=0 and y_conquer>=0):
                    if(self.board[x_conquer][y_conquer]==0):
                        moves_possible.append([x_conquer,y_conquer])
                        new_piece  = piece.Piece(x_conquer, y_conquer, curr_piece.color)
                        self.get_possible_moves(new_piece,moves_possible)
            