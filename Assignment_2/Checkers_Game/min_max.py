import min_max_game
import pygame
import values
import game
import board
import time

# Setting the dimensions of the window
window = pygame.display.set_mode((values.WIDTH+values.OPTIONS_PANEL_SIZE, values.HEIGHT))
# Adding a name to the window
pygame.display.set_caption("Checker's Game with Min Max")

# pygame.draw.rect(window, values.BUTTON_COLOR, (values.BLOCK_SIZE*values.ROWS + values.OPTIONS_PANEL_SIZE//2, values.ROWS//3*values.BLOCK_SIZE,values.BLOCK_SIZE*2, values.BLOCK_SIZE//2))

def play_ai(myGame):
    value, new_board = min_max_game.minmax(myGame.get_board(), 2, values.BLUE, myGame)
    myGame.play_ai(new_board)
    myGame.change_chance()

def random_game(myGame):    
    myGame.play_random()
    myGame.change_chance()

def two_player_game(myGame):

    myGame.change_chance()

# Main driver function
def ai_play():
    # Playing as true initially
    playing = True
    
    # # TEsting basic display
    # new_board = board.game_Board()
    # new_board.draw_blocks(window)
    # pygame.display.update()

    myGame = game.playGame(window)
    myGame.update()

        

    # Think over it to stop min max
    user = True
    while playing:

        # if myGame.chance == values.BLUE and not user:
        if myGame.chance == values.BLUE:
            play_ai(myGame)
            # user = True 
            
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
                        myGame = game.playGame(window)
                        random_play()

                    if(option ==2):
                        myGame = game.playGame(window)
                        ai_play()
                        # Min MAx

                        pass
                    if(option==4):
                        myGame = game.playGame(window)
                        two_player_play()

                    if(option==3):
                        # Restart
                        myGame = game.playGame(window)
                    if(option==5):
                        # Quit
                        myGame = game.playGame(window)
                        pygame.quit()

                    
                else:
                    row, column = get_mouse_position(position)
                    user = myGame.select_or_move(column, row)
                    user = not user

        myGame.update()

            
    pygame.quit()

def random_play():
    # Playing as true initially
    playing = True
    
    # # TEsting basic display
    # new_board = board.game_Board()
    # new_board.draw_blocks(window)
    # pygame.display.update()

    myGame = game.playGame(window)
    myGame.update()

        

    # Think over it to stop min max
    user = True
    while playing:

        # if myGame.chance == values.BLUE and not user:
        if myGame.chance == values.BLUE:
            random_game(myGame)            
            # user = True 
            
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
                        myGame = game.playGame(window)
                        random_play()

                    if(option ==2):
                        myGame = game.playGame(window)
                        ai_play()
                        # Min MAx

                        pass
                    if(option==4):
                        myGame = game.playGame(window)
                        two_player_play()

                    if(option==3):
                        # Restart
                        myGame = game.playGame(window)
                    if(option==5):
                        # Quit
                        myGame = game.playGame(window)
                        pygame.quit()

                    
                else:
                    row, column = get_mouse_position(position)
                    user = myGame.select_or_move(column, row)
                    user = not user

        myGame.update()

            
    pygame.quit()

def get_mouse_position(position):
    a,b = position
    #250, 250 pixels

    row = a//values.BLOCK_SIZE
    column = b//values.BLOCK_SIZE
    return row, column


def two_player_play():
    # Playing as true initially
    playing = True
    
    # # TEsting basic display
    # new_board = board.game_Board()
    # new_board.draw_blocks(window)
    # pygame.display.update()

    myGame = game.playGame(window)
    myGame.update()

        

    # Think over it to stop min max
    user = True
    while playing:

            
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
                        myGame = game.playGame(window)
                        random_play()

                    if(option ==2):
                        myGame = game.playGame(window)
                        ai_play()
                        # Min MAx

                        pass
                    if(option==4):
                        myGame = game.playGame(window)
                        two_player_play()

                    if(option==3):
                        # Restart
                        myGame = game.playGame(window)
                    if(option==5):
                        # Quit
                        myGame = game.playGame(window)
                        pygame.quit()

                    
                else:
                    row, column = get_mouse_position(position)
                    user = myGame.select_or_move(column, row)
                    user = not user

        myGame.update()

            
    pygame.quit()


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
    
    # 2 Player
    x_0 = values.BLOCK_SIZE*values.ROWS + 2*values.OPTIONS_PANEL_SIZE//10
    y_0 = 2.5*(values.ROWS//3*values.BLOCK_SIZE)
    x_1 = x_0 + values.BLOCK_SIZE*2
    y_1 = y_0 + values.BLOCK_SIZE//2
    if(x >= x_0 and x <= x_1 and y >= y_0 and y <= y_1):
        # random
        print("2 Player")
        return 4
    

    # Quit
    x_0 = values.BLOCK_SIZE*values.ROWS + 2*values.OPTIONS_PANEL_SIZE//10
    y_0 = 3*(values.ROWS//3*values.BLOCK_SIZE)
    x_1 = x_0 + values.BLOCK_SIZE*2
    y_1 = y_0 + values.BLOCK_SIZE//2
    if(x >= x_0 and x <= x_1 and y >= y_0 and y <= y_1):
        # random
        print("Quit")
        return 5
        


