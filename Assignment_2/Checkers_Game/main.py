import min_max_game
import pygame
import values
import game
import board
FPS = 60

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
    clock = pygame.time.Clock()
    
    while playing:
        clock.tick(FPS)

        if myGame.chance == values.BLUE:
            value, new_board = min_max_game.minmax(myGame.get_board(), 1, values.BLUE, myGame)
            myGame.ai_move(new_board)
            
        if myGame.champion() != None:
            print(game.champion())
            run = False

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
                x = position[0]
                y = position[1]
                x = int(x)
                y = int(y)
    
                if(x>values.BLOCK_SIZE*(values.ROWS) or y>values.BLOCK_SIZE*(values.ROWS)):
                    option = get_option(x,y)
                    if(option == 1):
                        # Random
                        pass
                    if(option ==2):
                        # Min MAx
                        pass
                    if(option==3):
                        # Restart
                        myGame.reset()
                    if(option==5):
                        # Quit
                        pygame.quit()

                    
                else:
                    row, column = get_mouse_position(position)
                    myGame.select_or_move(column, row)
        myGame.update()

        
        pygame.display.update()
        
    pygame.quit()


def get_mouse_position(position):
    a,b = position
    #250, 250 pixels

    row = a//values.BLOCK_SIZE
    column = b//values.BLOCK_SIZE
    return row, column

def get_option(x,y):
    x = int(x)
    y = int(y)
    
    # Random
    x_0 = values.BLOCK_SIZE*values.ROWS + 2*values.OPTIONS_PANEL_SIZE//10
    y_0 = values.ROWS//3*values.BLOCK_SIZE
    
    x_1 = x_0 + values.BLOCK_SIZE*2
    y_1 = y_0 + values.BLOCK_SIZE//2

    
    if(x >= x_0 and x <= x_1 and y >= y_0 and y <= y_1):
        # random
        print("Random")
        return 1

    # Min max
    x_0 = values.BLOCK_SIZE*values.ROWS + 2*values.OPTIONS_PANEL_SIZE//10
    y_0 = 1.5*(values.ROWS//3*values.BLOCK_SIZE)
    x_1 = x_0 + values.BLOCK_SIZE*2
    y_1 = y_0 + values.BLOCK_SIZE//2
    if(x >= x_0 and x <= x_1 and y >= y_0 and y <= y_1):
        # random
        print("Min Max")
        return 2

    # Restart
    x_0 = values.BLOCK_SIZE*values.ROWS + 2*values.OPTIONS_PANEL_SIZE//10
    y_0 = 2*(values.ROWS//3*values.BLOCK_SIZE)
    x_1 = x_0 + values.BLOCK_SIZE*2
    y_1 = y_0 + values.BLOCK_SIZE//2
    if(x >= x_0 and x <= x_1 and y >= y_0 and y <= y_1):
        # random
        print("Restart")
        return 3
         
    # Quit
    x_0 = values.BLOCK_SIZE*values.ROWS + 2*values.OPTIONS_PANEL_SIZE//10
    y_0 = 3*(values.ROWS//3*values.BLOCK_SIZE)
    x_1 = x_0 + values.BLOCK_SIZE*2
    y_1 = y_0 + values.BLOCK_SIZE//2
    if(x >= x_0 and x <= x_1 and y >= y_0 and y <= y_1):
        # random
        print("Quit")
        return 5
        


main()