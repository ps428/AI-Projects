import copy
import pygame
import values

def minmax(board_state, depth, max_player, game):
    if depth == 0 or board_state.champion() != None:
        return board_state.evaluation_function(), board_state
    
    if max_player:
        max_score = float('-inf')
        ideal_move = None
        for move in get_all_moves(board_state, values.BLUE, game):
            score = minmax(move, depth-1, False, game)[0]
            max_score = max(max_score, score)
            if max_score == score:
                ideal_move = move
        return max_score, ideal_move

    else:
        min_score = float('inf')
        ideal_move = None
        for move in get_all_moves(board_state, values.RED, game):
            score = minmax(move, depth-1, True, game)[0]
            print(min_score, score)
            min_score = min(min_score, score)
            if min_score == score:
                ideal_move = move
        return min_score, ideal_move

def get_all_moves(board_state, color, game):
    moves = []
    for piece in board_state.get_all_pieces_colorwise(color):
        valid_moves = board_state.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            draw_moves(game, board_state, piece)

            curr_board = copy.deepcopy(board_state)
            curr_piece = curr_board.get_piece(piece.row, piece.column)
            new_board_state = simulation(curr_piece, move, curr_board, game, skip)
            moves.append(new_board_state)
    return moves

def simulation(piece, move, board, game, skip):
    board.make_move(piece, move[0], move[1])
    if skip:
        board.kill(skip)
    return board

def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw_blocks(game.window)
    pygame.draw.circle(game.window, (0,255,0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()