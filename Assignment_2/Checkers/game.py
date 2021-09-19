import pygame
import game_values
import game_board

WINDOW = pygame.display.set_mode((game_values.WIDTH, game_values.HEIGHT))
pygame.display.set_caption("Checkers Game")

def get_pos_mous_event(position):
    x,y = position
    row = y//game_values.SQUARE_SIZE
    column = x//game_values.SQUARE_SIZE

    return row, column

def main():
    play = 1
    board = game_board.game_Board()

    # Cheking basic piece movement
    # piece = board.get_piece(2,0)
    # board.move(piece, 4,4)

    while play:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = 0 # end the game
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                row, column = get_pos_mous_event(position)
                piece = board.get_piece(row, column)
                # A fixed move for testing purpose
                board.move(piece, 4, 4)
            
        board.draw_all(WINDOW)
        pygame.display.update()

    pygame.quit()

main()