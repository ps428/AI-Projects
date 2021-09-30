import pygame
import values
import board

class playGame:
    def __init__(self, window):
        self.active_piece = None
        self.board = board.game_Board()
        self.chance = values.RED
        self.window = window
        self.valid_positions = {}

    def update(self):
        self.board.current_status(self.window)
        self.draw_valid_moves(self.valid_positions)
        pygame.display.update()
    
    def reset(self):
        self.active_piece = None
        self.board = board.game_Board()
        self.chance = values.BLUE
        self.valid_positions = {}
        self.update()
    
    # def select_or_move(self, x,y):
    #     if self.active_piece==None or self.active_piece==0:
    #         print("vacant",self.active_piece)
    #         self.active_piece = self.board.get_piece(x,y)
    #         self.draw_possible_moves(self.active_piece)
    #         self.valid_positions = self.board.get_valid_moves(self.active_piece)

    #     else:
    #         print("peice: ",self.active_piece.row, self.active_piece.column)
    #         if(x==self.active_piece.row and y == self.active_piece.column):
    #             self.active_piece = None
    #             print("reset selection")
    #             self.update()
    #             return
    
    #         self.valid_positions = self.board.get_valid_moves(self.active_piece)

    #         if (x,y) in self.valid_positions:
    #             print("valid pos:" ,self.valid_positions)
    #             deads = self.valid_positions[(x,y)]
    #             if deads:
    #                 self.board.kill(deads)
    #             self.make_move(x,y)
    #             self.update()
            
    # def make_move(self, x, y):
    #     # print("from:",self.active_piece.row,self.active_piece.column)
    #     # print("to:",x,y)
    #     if self.board.board[x][y] != 0:
    #         self.active_piece = None
    #         return

    #     self.board.make_move(self.active_piece, x, y)
    #     # self.active_piece.move(x,y)
    #     self.active_piece = None
    #     self.change_chance()

        

    def select_or_move(self, row, col):
        if self.active_piece:
            result = self.move(row, col)
            if not result:
                self.active_piece = None
                self.select_or_move(row, col)
        
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.chance:
            self.active_piece = piece
            self.valid_positions = self.board.get_valid_moves(piece)
            return True
            
        return False

    def move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.active_piece: 
            if piece == 0:
                if (row, col) in self.valid_positions:
                    self.board.make_move(self.active_piece, row, col)
                    skipped = self.valid_positions[(row, col)]
                    if skipped:
                        self.board.kill(skipped)
                    self.change_chance()
        else:
            return False

        return True

    def change_chance(self):
        if self.chance == values.RED:
            self.chance = values.BLUE
        else:
            self.chance = values.RED
        # resetting the valid positions to empty dictionary
        self.valid_positions = {}

    # // TODO drawing possible moves
    def draw_possible_moves(self,piece):
        moves = self.board.get_possible_moves(piece, [], False)
        if(moves!=None):
            print(moves)
            for move in moves:
                print(move)
                if move is not None and len(move) == 2:
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
    
    
    def get_board(self):
        return self.board
    
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            x = move[1] * values.BLOCK_SIZE + values.BLOCK_SIZE//2
            y = move[0] * values.BLOCK_SIZE + values.BLOCK_SIZE//2
            # print("circle")
            pygame.draw.circle(self.window, values.CHANCE, (x,y), values.BLOCK_SIZE//8)
            pygame.draw.circle(self.window, values.CHANCE, (x,y), values.BLOCK_SIZE//2,2)

    def champion(self):
        return self.board.champion()

    
    def play_ai(self, board):
        self.board = board
        print("AI move")
    
    def play_random(self):
        print("Random move")

    
    def two_player(self):
        print("Two Player move")
        