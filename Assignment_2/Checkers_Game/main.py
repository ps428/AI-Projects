import pygame
import values
import game
import board

# Setting the dimensions of the window
window = pygame.display.set_mode((values.WIDTH+values.OPTIONS_PANEL_SIZE, values.HEIGHT))
# Adding a name to the window
pygame.display.set_caption("Checker's Game with Min Max")

# pygame.draw.rect(window, values.BUTTON_COLOR, (values.BLOCK_SIZE*values.ROWS + values.OPTIONS_PANEL_SIZE//2, values.ROWS//3*values.BLOCK_SIZE,values.BLOCK_SIZE*2, values.BLOCK_SIZE//2))


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
                x,y = position
                if(x>values.BLOCK_SIZE*(values.ROWS) or y>values.BLOCK_SIZE*(values.ROWS)):
                    pass
                else:
                    row, column = get_mouse_position(position)
                    myGame.select_or_move(column, row)
                
        
        pygame.display.update()
        
    pygame.quit()




def get_mouse_position(position):
    a,b = position
    #250, 250 pixels

    row = a//values.BLOCK_SIZE
    column = b//values.BLOCK_SIZE
    print(row, column)
    return row, column

main()