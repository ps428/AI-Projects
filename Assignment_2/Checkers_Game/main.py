import pygame
import values
import game
import board

# Setting the dimensions of the window
window = pygame.display.set_mode((values.WIDTH, values.HEIGHT))
# Adding a name to the window
pygame.display.set_caption("Checker's Game with Min Max")

# Main driver function
def main():
    # Playing as true initially
    playing = True
    
    # # TEsting basic display
    # new_board = board.game_Board()
    # new_board.draw_blocks(window)
    # pygame.display.update()

    myGame = game.playGame(window)
    myGame.update()
    while playing:

        # Look at the events being triggered by the user in the game
        for event in pygame.event.get():
            # If a event to end the game is triggered, then quit the game
            if event.type == pygame.QUIT:
                playing = False
        
            # If the event is mouse button cliked, then do something
            # NOTE: MOUSEBUTTONDOWN => button is clicked
            #       MOUSEBUTTONUP   => button is released
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                row, column = get_mouse_position(position)
                myGame.select_or_move(column, row)
                
        
        pygame.display.update()
        
    pygame.quit()




def get_mouse_position(position):
    a,b = position

    row = a//values.BLOCK_SIZE
    column = b//values.BLOCK_SIZE
    print(row, column)
    return row, column

main()