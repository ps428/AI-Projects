import pygame
import values
import game
import board
import time
import copy

depth = 3
# Setting the dimensions of the window
window = pygame.display.set_mode((values.WIDTH+values.OPTIONS_PANEL_SIZE, values.HEIGHT))
# Adding a name to the window
pygame.display.set_caption("Checker's Game with Min Max")

# pygame.draw.rect(window, values.BUTTON_COLOR, (values.BLOCK_SIZE*values.ROWS + values.OPTIONS_PANEL_SIZE//2, values.ROWS//3*values.BLOCK_SIZE,values.BLOCK_SIZE*2, values.BLOCK_SIZE//2))

# ai game type
def play_ai(myGame):
    value, new_board = minmax( depth, values.BLUE, myGame, myGame.get_board())
    myGame.play_ai(new_board)
    myGame.change_chance()

# ramdom game type
def random_game(myGame):
    CPU_pieces = myGame.board.get_all_pieces_colorwise(values.BLUE)  
    myGame.play_random(CPU_pieces)
    myGame.change_chance()

# 2 player game type
def two_player_game(myGame):

    myGame.change_chance()

# driver function
def ai_play():
    # Playing as true initially
    playing = True
    no_kill_moves = 0
    
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
            count_red = myGame.board.player_count_red
            count_blue = myGame.board.player_count_blue
            play_ai(myGame)
            count_red_moved = myGame.board.player_count_red
            count_blue_moved = myGame.board.player_count_blue
            no_kill_moves+=1
            if(count_blue!=count_blue_moved or count_red!=count_red_moved):
                no_kill_moves = 0
            
            
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
                    count_red = myGame.board.player_count_red
                    count_blue = myGame.board.player_count_blue
                    user = myGame.select_or_move(column, row)
                    count_red_moved = myGame.board.player_count_red
                    count_blue_moved = myGame.board.player_count_blue
                    no_kill_moves+=1
                    if(count_blue!=count_blue_moved or count_red!=count_red_moved):
                        no_kill_moves = 0
                    if draw_condition(no_kill_moves):
                        draw_game(myGame)
                    
                    user = not user

        myGame.update()

            
    pygame.quit()

def random_play():
    # Playing as true initially
    no_kill_moves = 0
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
            
            count_red = myGame.board.player_count_red
            count_blue = myGame.board.player_count_blue
            random_game(myGame)            
            count_red_moved = myGame.board.player_count_red
            count_blue_moved = myGame.board.player_count_blue
            no_kill_moves+=1
            if(count_blue!=count_blue_moved or count_red!=count_red_moved):
                no_kill_moves = 0
            # user = True 
            
            # if winnder, then end
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
                    count_red = myGame.board.player_count_red
                    count_blue = myGame.board.player_count_blue
                    user = myGame.select_or_move(column, row)
                    count_red_moved = myGame.board.player_count_red
                    count_blue_moved = myGame.board.player_count_blue
                    no_kill_moves+=1
                    if(count_blue!=count_blue_moved or count_red!=count_red_moved):
                        no_kill_moves = 0
                    if draw_condition(no_kill_moves):
                        draw_game(myGame)
                    
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
    no_kill_moves = 0
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
                    count_red = myGame.board.player_count_red
                    count_blue = myGame.board.player_count_blue
                    user = myGame.select_or_move(column, row)
                    count_red_moved = myGame.board.player_count_red
                    count_blue_moved = myGame.board.player_count_blue
                    no_kill_moves+=1
                    print(no_kill_moves)
                    if(count_blue!=count_blue_moved or count_red!=count_red_moved):
                        no_kill_moves = 0
                    if draw_condition(no_kill_moves):
                        myGame.board.draw_game_now(window)
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
        

# function to check for draw
def draw_condition(no_kills):
    if no_kills>=50:
        return True
    return False

# function to draw the "Draw on the board"
def draw_game(myGame):
    x = values.BLOCK_SIZE*values.ROWS + 2*values.OPTIONS_PANEL_SIZE//10
    y = values.ROWS//3*values.BLOCK_SIZE
    print("draww")
    font = pygame.font.SysFont(None, 48)
    img1 = font.render('Game Drawn', True, values.OPTION_TEXT)
    window.blit(img1, (x-30,y-10))
    pygame.draw.circle(window, values.OPTION_TEXT, (x,y), 10)
    pygame.display.update()
    # myGame = game.playGame()

# to similate the moves
def make_test_move( move, board,  skip, piece):
    board.make_move(piece, move[0], move[1])
    if skip:
        board.kill(skip)
    return board

    

# gets all the moves possible for all pieces of the board by making a clone,
#  pass by value of the current board
def get_all_moves(board_state, color, game):
    # list having all the possible moves
    moves = []
    for piece in board_state.get_all_pieces_colorwise(color):
        valid_moves = board_state.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            draw_moves( board_state, piece, game)

            # pass by value, deepcopy of the current board
            # object of board class
            curr_board = copy.deepcopy(board_state)
            curr_piece = curr_board.get_piece(piece.row, piece.column)
            new_board_state = make_test_move( move, curr_board,  skip, curr_piece)
            # appending the moves 
            moves.append(new_board_state)
    # returning the possible moves
    return moves

# to draw out the current possible moves tried
def draw_moves( board, piece, game):
    # drawing the board first
    board.draw_blocks(game.window)
    # getting the valid moves for the piece
    valid_moves = board.get_valid_moves(piece)
    pygame.draw.circle(game.window, values.OPTIONS_PANEL, (piece.x, piece.y), 50, 2)
    # draing the valid moves
    game.draw_valid_moves(valid_moves.keys())
    #updating the pygame
    pygame.display.update()


def minmax( depth, max_player, game, board_state):

    # using evaluation function to enhance the ai
    if depth == 0 or board_state.champion() != None:
        # when depth is 0, return the evaluation score and current state of the board
        return board_state.evaluation_function(), board_state
    

    # max case
    if max_player:
        ideal_move = None
        # setting max score to minimum
        max_score = -99999.99
        # iterating over all the vlue values, ai pieces
        for move in get_all_moves(board_state, values.BLUE, game):
            score = minmax( depth-1, False, game, move)[0]
            # applyling max to get highest value
            max_score = max(max_score, score)
            if max_score == score:
                ideal_move = move
        # returning the max score and the move causing it
        return max_score, ideal_move

    # min case
    else:
        ideal_move = None
        # setting min score to maximum
        min_score = 99999.99
        # iterating over all the red values, human pieces
        for move in get_all_moves(board_state, values.RED, game):
            score = minmax( depth-1, True, game, move)[0]
            # applyling min to get lowest value
            min_score = min(min_score, score)
            if min_score == score:
                ideal_move = move

        # returning the min score and the move causing it
        return min_score, ideal_move

