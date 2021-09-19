import pygame
import game_board
import game_values

class play_Game:
    def __init__(self, window):
        self.piece_active = None # No active piece selected for now
        self.board = game_board.game_Board()
        self.chance = game_values.RED
        self.valid_moves = {}
        self.window = window

    def update(self):
        self.board.draw_all(self.window)
        pygame.display.update()

    def reset(self):
        self.piece_active = None # No active piece selected for now
        self.board = game_board.game_Board()
        self.chance = game_values.RED
        self.valid_moves = {}
        
    def select(self, row, column):
        if self.piece_active:
            result = self.move(row, column)
            if not result:
                self.piece_active = None
                self.select(row, column)
        else:
            piece = self.board.get_piece(row, column)
            if piece != 0 and piece.color == self.turn:
                self.piece_active = piece
                self.valid_moves = self.board.get_valid_moves(piece)        
                return True

        return False

    def move(self, row, column):
        piece = self.board.get_piece(row, column)
        if self.piece_active and piece == 0 and (row, column) in self.valid_moves:
            self.board.move(self.piece_active, row, column)
            self.change_turn()
        else:
            return False
        return True

    def change_turn(self):
        if self.chance == game_values.RED:
            self.chance = game_values.WHITE
        else:
            self.chance = game_values.RED
