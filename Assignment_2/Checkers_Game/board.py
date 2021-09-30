from typing import Collection
import pygame
import piece
import values

class game_Board:
    def __init__(self):
        self.board = []
        self.player_count_blue = 12
        self.player_count_red = 12
        self.kings_count_blue = 0
        self.kings_count_red = 0
        self.kill_or_not = False
        self.make_pieces()
        
    def fill_block(window, row, column):
        # Fill a rectangle at row, column with height and width equal to BLOCK_SIZE
        pygame.draw.rect(window, values.LIGHT, (row*values.BLOCK_SIZE, column*values.BLOCK_SIZE, values.BLOCK_SIZE, values.BLOCK_SIZE))

    def draw_blocks(self, window):
        window.fill(values.DARK)

        #OPTIONS PANE
        pygame.draw.rect(window, values.OPTIONS_PANEL, (values.BLOCK_SIZE*values.ROWS, 0, values.OPTIONS_PANEL_SIZE+10, values.ROWS*values.BLOCK_SIZE +10))
        pygame.init()
        
        #Buttons
        # Random Game
        x = values.BLOCK_SIZE*values.ROWS + 2*values.OPTIONS_PANEL_SIZE//10
        y = values.ROWS//3*values.BLOCK_SIZE
        font = pygame.font.SysFont(None, 48)
        img1 = font.render('Checkers Game', True, values.OPTION_TEXT)
        window.blit(img1, (x-30,y-80))

        
        pygame.draw.rect(window, values.BLACK, (x, y, values.BLOCK_SIZE*2, values.BLOCK_SIZE//2),8)
        pygame.draw.rect(window, values.BUTTON_COLOR, (x, y, values.BLOCK_SIZE*2, values.BLOCK_SIZE//2))
        font = pygame.font.SysFont(None, 32)
        img1 = font.render('Random Game', True, values.BUTTON_TEXT_COLOR)
        window.blit(img1, (x+10,y+10))


        # Min Max Game
        x = values.BLOCK_SIZE*values.ROWS + 2*values.OPTIONS_PANEL_SIZE//10
        y = 1.5*(values.ROWS//3*values.BLOCK_SIZE)
        pygame.draw.rect(window, values.BLACK, (x, y, values.BLOCK_SIZE*2, values.BLOCK_SIZE//2),8)
        pygame.draw.rect(window, values.BUTTON_COLOR, (x, y, values.BLOCK_SIZE*2, values.BLOCK_SIZE//2))
        img1 = font.render('MiniMax', True, values.BUTTON_TEXT_COLOR)
        window.blit(img1, (x+45,y+10))
        
        # Restart
        x = values.BLOCK_SIZE*values.ROWS + 2*values.OPTIONS_PANEL_SIZE//10
        y = 2*(values.ROWS//3*values.BLOCK_SIZE)
        pygame.draw.rect(window, values.BLACK, (x, y, values.BLOCK_SIZE*2, values.BLOCK_SIZE//2),8)
        pygame.draw.rect(window, values.BUTTON_COLOR, (x, y, values.BLOCK_SIZE*2, values.BLOCK_SIZE//2))
        img1 = font.render('Restart Game', True, values.BUTTON_TEXT_COLOR)
        window.blit(img1, (x+20,y+10))

        # 2 Player 
        x = values.BLOCK_SIZE*values.ROWS + 2*values.OPTIONS_PANEL_SIZE//10
        y = 2.5*(values.ROWS//3*values.BLOCK_SIZE)
        pygame.draw.rect(window, values.BLACK, (x, y, values.BLOCK_SIZE*2, values.BLOCK_SIZE//2),8)
        pygame.draw.rect(window, values.BUTTON_COLOR, (x, y, values.BLOCK_SIZE*2, values.BLOCK_SIZE//2))
        img1 = font.render('2 Player', True, values.BUTTON_TEXT_COLOR)
        window.blit(img1, (x+45,y+10))

        # Quit
        x = values.BLOCK_SIZE*values.ROWS + 2*values.OPTIONS_PANEL_SIZE//10
        y = 3*(values.ROWS//3*values.BLOCK_SIZE)
        pygame.draw.rect(window, values.BLACK, (x, y, values.BLOCK_SIZE*2, values.BLOCK_SIZE//2),8)
        pygame.draw.rect(window, values.BUTTON_COLOR, (x, y, values.BLOCK_SIZE*2, values.BLOCK_SIZE//2))
        img1 = font.render('Quit Game', True, values.BUTTON_TEXT_COLOR)
        window.blit(img1, (x+30,y+10))

        img1 = font.render('SCOREBOARD', True, values.OPTIONS_SCORECARD)
        window.blit(img1, (x+10,y+60))
        
        x += 20
        score_blue  ="Blue"
        img1 = font.render(score_blue, True, values.OPTIONS_SCORECARD)
        window.blit(img1, (x,y+90))

        score_red  ="Red"
        img1 = font.render(score_red, True, values.OPTIONS_SCORECARD)
        window.blit(img1, (x+85,y+90))

        term = "Score"
        img1 = font.render(term, True, values.OPTIONS_SCORECARD)
        window.blit(img1, (x-70,y+120))

        score_blue  = str(12 - self.player_count_blue)
        img1 = font.render(score_blue, True, values.OPTIONS_SCORECARD)
        window.blit(img1, (x+20,y+120))

        score_red  = str(12 - self.player_count_red)
        img1 = font.render(score_red, True, values.OPTIONS_SCORECARD)
        window.blit(img1, (x+100,y+120))

        term = "Kings"
        img1 = font.render(term, True, values.OPTIONS_SCORECARD)
        window.blit(img1, (x-70,y+150))

        score_blue  = str(self.kings_count_blue)
        img1 = font.render(score_blue, True, values.OPTIONS_SCORECARD)
        window.blit(img1, (x+20,y+150))

        score_red  = str(self.kings_count_red)
        img1 = font.render(score_red, True, values.OPTIONS_SCORECARD)
        window.blit(img1, (x+100,y+150))

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
            piece.make_king()
            piece.king = True

            if piece.color == values.BLUE:
                self.kings_count_blue+=1
            else:
                self.kings_count_red+=1
        
    def check_kill(self, curr_piece, x, y):
        kill = False
        x_0 = x - curr_piece.row 
        y_0 = y - curr_piece.column

        filled_piece = self.board[x_0][y_0] 
        if filled_piece != 0:
            if filled_piece.color != curr_piece.color:
                if self.board[x][y]==0:
                    self.board[x_0][y_0] = 0 
                    self.board[curr_piece.row][curr_piece.column] = 0
                    self.board[x][y] = curr_piece
        
    def current_status(self, window):
        self.draw_blocks(window)
        for row in range(0, values.ROWS):
            for column in range(0, values.COLUMNS):
                piece = self.board[row][column]
                if piece != 0:
                    piece.draw_piece(window)

# TODO OUT OF MIND
    def get_possible_moves(self, curr_piece, moves_possible, is_recursive):
       # to break just becoming the king, break if the moves_possible is null and king ==true
        if(curr_piece != 0):
            skipped = []
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
                        if(not is_recursive):
                            if(self.board[x_p][y_p]==0):
                                moves_possible.append([x_p,y_p])
                                print("Blue | Forward | Right")
                            else:
                                filled_piece = self.board[x_p][ y_p]
                                is_right = True
                                new_moves = self._move_positive(curr_piece, moves_possible, filled_piece, is_right)  
                                
                                moves_possible.append(new_moves)
                        elif(self.board[x_p][y_p]!=0):
                            filled_piece = self.board[x_p][ y_p]
                            is_right = True
                            new_moves = self._move_positive(curr_piece, moves_possible, filled_piece, is_right)  
                            moves_possible.append(new_moves)
                        

                    if(y_n>=0 and x_p<=7):
                        # if(self.board[x_n][y_p]==0): # none case
                        if(not is_recursive):
                            if(self.board[x_p][y_n]==0): 
                                print("Blue | Forward | Left")
                                moves_possible.append([x_p,y_n])
                            else:
                                filled_piece = self.board[x_p][y_n]
                                is_right = False
                                new_moves = self._move_positive(curr_piece, moves_possible, filled_piece, is_right)  
                                moves_possible.append(new_moves)
                        elif(self.board[x_p][y_n]!=0):
                            filled_piece = self.board[x_p][y_n]
                            is_right = False
                            new_moves = self._move_positive(curr_piece, moves_possible, filled_piece, is_right)  
                            moves_possible.append(new_moves)

                else:
                    stance = False    
                    if(y_p<=7 and x_n>=0):
                        # print("Red | Backward | Right")
                        if(not is_recursive):
                            if(self.board[x_n][y_p]==0):
                                print("Red | Backward | Right")
                                moves_possible.append([x_n,y_p])
                            else:
                                filled_piece = self.board[x_n][y_p]
                                is_right = True
                                new_moves = self._move_negative(curr_piece, moves_possible, filled_piece, is_right)  
                                moves_possible.append(new_moves)
                        elif(self.board[x_n][y_p]!=0):
                            filled_piece = self.board[x_n][y_p]
                            is_right = True
                            new_moves = self._move_negative(curr_piece, moves_possible, filled_piece, is_right)  
                            moves_possible.append(new_moves)

                    if(x_n>=0 and y_n>=0):
                        # print("Red | Backward | Left")
                        if(not is_recursive):
                            if(self.board[x_n][y_n]==0):
                                print("Red | Backward | Left")
                                moves_possible.append([x_n,y_n])
                            else:
                                filled_piece = self.board[x_n][y_n]
                                is_right = False
                                new_moves = self._move_negative(curr_piece, moves_possible, filled_piece, is_right)  
                                moves_possible.append(new_moves)
                        elif(self.board[x_n][y_n]!=0):
                            filled_piece = self.board[x_n][y_n]
                            is_right = False
                            new_moves = self._move_negative(curr_piece, moves_possible, filled_piece, is_right)  
                            moves_possible.append(new_moves)
                
            # King case
            else: 
                x = curr_piece.row
                y = curr_piece.column
                x_p = x+1
                y_p = y+1
                x_n = x-1
                y_n = y-1
                stance =True
                # if forward elements are non zero, get possible moves
                if(x_p<=7 and y_p<=7):
                    if(not is_recursive):
                        if(self.board[x_p][y_p]==0):
                            moves_possible.append([x_p,y_p])
                            print("Blue | Forward | Right")
                        else:
                            filled_piece = self.board[x_p][ y_p]
                            is_right = True
                            new_moves = self._move_positive(curr_piece, moves_possible, filled_piece, is_right)  
                            moves_possible.append(new_moves)
                    elif(self.board[x_p][y_p]!=0):
                        filled_piece = self.board[x_p][ y_p]
                        is_right = True
                        new_moves = self._move_positive(curr_piece, moves_possible, filled_piece, is_right)  
                        moves_possible.append(new_moves)

                if(y_n>=0 and x_p<=7):
                    # if(self.board[x_n][y_p]==0): # none case
                    if(not is_recursive):
                        if(self.board[x_p][y_n]==0): 
                            print("Blue | Forward | Left")
                            moves_possible.append([x_p,y_n])
                        else:
                            filled_piece = self.board[x_p][y_n]
                            is_right = False
                            new_moves = self._move_positive(curr_piece, moves_possible, filled_piece, is_right)  
                            moves_possible.append(new_moves)
                    elif(self.board[x_p][y_n]!=0):
                        filled_piece = self.board[x_p][y_n]
                        is_right = False
                        new_moves = self._move_positive(curr_piece, moves_possible, filled_piece, is_right)  
                        moves_possible.append(new_moves)

                stance = False    
                if(y_p<=7 and x_n>=0):
                    # print("Red | Backward | Right")
                    if(not is_recursive):
                        if(self.board[x_n][y_p]==0):
                            print("Red | Backward | Right")
                            moves_possible.append([x_n,y_p])
                        else:
                            filled_piece = self.board[x_n][y_p]
                            is_right = True
                            new_moves = self._move_negative(curr_piece, moves_possible, filled_piece, is_right)  
                            moves_possible.append(new_moves)
                    elif(self.board[x_n][y_p]!=0):
                        filled_piece = self.board[x_n][y_p]
                        is_right = True
                        new_moves = self._move_negative(curr_piece, moves_possible, filled_piece, is_right)  
                        moves_possible.append(new_moves)

                if(x_n>=0 and y_n>=0):
                    # print("Red | Backward | Left")
                    if(not is_recursive):
                        if(self.board[x_n][y_n]==0):
                            print("Red | Backward | Left")
                            moves_possible.append([x_n,y_n])
                        else:
                            filled_piece = self.board[x_n][y_n]
                            is_right = False
                            new_moves = self._move_negative(curr_piece, moves_possible, filled_piece, is_right)  
                            moves_possible.append(new_moves)
                    elif(self.board[x_n][y_n]!=0):
                        filled_piece = self.board[x_n][y_n]
                        is_right = False
                        new_moves = self._move_negative(curr_piece, moves_possible, filled_piece, is_right)  
                        moves_possible.append(new_moves)
                    
                pass
        return moves_possible

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
                        self.get_possible_moves(new_piece,moves_possible, True)
           
            else:
                x_conquer = filled_piece.row + 1
                y_conquer = filled_piece.column - 1
                if(x_conquer<=7 and y_conquer>=0):
                    if(self.board[x_conquer][y_conquer]==0):
                        moves_possible.append([x_conquer,y_conquer])
                        new_piece  = piece.Piece(x_conquer, y_conquer, curr_piece.color)
                        self.get_possible_moves(new_piece,moves_possible, True)
            if len(moves_possible) is 2:
                return moves_possible
        
    def _move_negative(self, curr_piece, moves_possible, filled_piece, is_right):
        if(curr_piece.color != filled_piece.color):
            if(is_right):
                x_conquer = filled_piece.row - 1
                y_conquer = filled_piece.column + 1
                if(x_conquer>=0 and y_conquer<=7):
                    if(self.board[x_conquer][y_conquer]==0):
                        moves_possible.append([x_conquer,y_conquer])
                        new_piece  = piece.Piece(x_conquer, y_conquer, curr_piece.color)
                        self.get_possible_moves(new_piece,moves_possible, True)
            else:
                x_conquer = filled_piece.row - 1
                y_conquer = filled_piece.column - 1
                if(x_conquer>=0 and y_conquer>=0):
                    if(self.board[x_conquer][y_conquer]==0):
                        moves_possible.append([x_conquer,y_conquer])
                        new_piece  = piece.Piece(x_conquer, y_conquer, curr_piece.color)
                        self.get_possible_moves(new_piece,moves_possible, True)
            if len(moves_possible) is 2:
                return moves_possible
    
    def kill(self, pieces):
         for piece in pieces:
            if piece.king:
                if  piece.color == values.RED:
                    self.kings_count_red -= 1
                else:
                    self.kings_count_blue -= 1        
            

            self.board[piece.row][piece.column] = 0
            if piece != 0:
                values.aud_kill_made.play()
            
                if piece.color == values.BLUE:
                    self.player_count_red -= 1
                else:
                    self.player_count_blue -= 1

    def evaluation_function(self):
        #basic score
        score = self.player_count_blue - self.player_count_red
        #a little better scoring by considering kings
        score += 0.5*(self.kings_count_blue - self.kings_count_red)
        # TODO can work here for better AI
        return score

    def champion(self):
        if self.player_count_red <=0:
            return values.BLUE
        elif self.player_count_blue <=0:
            return values.RED
        else:
            return None

    def get_valid_moves(self, piece):
        moves = {}
        if piece == 0:
            return
        left = piece.column - 1
        right = piece.column + 1
        row = piece.row

        if piece.color == values.RED or piece.king:
            moves.update(self._traverse_left(row -1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row -1, max(row-3, -1), -1, piece.color, right))
        if piece.color == values.BLUE or piece.king:
            moves.update(self._traverse_left(row +1, min(row+3, values.ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row +1, min(row+3, values.ROWS), 1, piece.color, right))
    
        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, values.ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, left-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, left+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1
        
        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= values.COLUMNS:
                break
            
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,right)] = last + skipped
                else:
                    moves[(r, right)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, values.ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, right-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, right+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1
        
        return moves