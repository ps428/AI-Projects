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
            self.draw_possible_moves(self.active_piece)
        else:
            print("peice: ",self.active_piece.row, self.active_piece.column)
            if(x==self.active_piece.row and y == self.active_piece.column):
                self.active_piece = None
                print("reset selection")
                self.update()
                return
            if (x,y) in self.board.get_valid_moves(self.active_piece).keys():
                self.make_move(x,y)
                self.update()
            

    def make_move(self, x, y):
        # print("from:",self.active_piece.row,self.active_piece.column)
        # print("to:",x,y)
        if self.board.board[x][y] != 0:
            self.active_piece = None
            return

        self.board.make_move(self.active_piece, x, y)
        # self.active_piece.move(x,y)
        self.active_piece = None

    def change_chance(self):
        if self.chance == values.RED:
            self.chance = values.BLUE
        else:
            self.chance = values.BLUE


    # // TODO drawing possible moves
    def draw_possible_moves(self,piece):
        moves = self.board.get_possible_moves(piece, [], False)
        if(moves!=None):
            print(moves)
            for move in moves:
                print(move)
                if move is not None and len(move) is 2:
                    x = move[1] * values.BLOCK_SIZE + values.BLOCK_SIZE//2
                    y = move[0] * values.BLOCK_SIZE + values.BLOCK_SIZE//2
                    # print("circle")
                    pygame.draw.circle(self.window, values.CHANCE, (x,y), values.BLOCK_SIZE//8)
                    pygame.display.update()
        moves = self.board.get_valid_moves(piece)
        if(moves!=None):
            for move in moves:
                x = move[1] * values.BLOCK_SIZE + values.BLOCK_SIZE//2
                y = move[0] * values.BLOCK_SIZE + values.BLOCK_SIZE//2
                # print("circle")
                pygame.draw.circle(self.window, values.CHANCE, (x,y), values.BLOCK_SIZE//8)
                pygame.draw.circle(self.window, values.CHANCE, (x,y), values.BLOCK_SIZE//2,2)
                pygame.display.update()