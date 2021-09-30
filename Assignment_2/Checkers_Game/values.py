import pygame
pygame.init()
pygame.font.init()
pygame.mixer.init() 

# audio files initialisations
aud_king_made = pygame.mixer.Sound('king.wav')
aud_movement_mode = pygame.mixer.Sound('move.wav')
aud_kill_made = pygame.mixer.Sound('kill.wav')


HEIGHT = 700
WIDTH = 700

# COLORS
RED = (220,20,60)


BLUE = 	(139,0,139)

BLACK = (0,0,0)
WHITE = (255,255,255)
LIGHT = (240,255,240)

CHANCE = (137, 207, 240)
# LIGHT = (255,210,180)
KING = (255,215,0)

# DARK = (80,235,130)
DARK = (32,178,170)

# DARK = (80,235,130) # 2
# DARK = (140,235,170) # 1

OPTIONS_PANEL_SIZE = HEIGHT//2
OPTIONS_PANEL = (66, 5, 22) 
BUTTON_COLOR = (255,112,102)
OPTION_TEXT = (240, 165, 0)
BUTTON_TEXT_COLOR = (0,0,0)
OPTIONS_SCORECARD = (244, 59, 134)
ROWS = 8
COLUMNS = 8
BLOCK_SIZE = HEIGHT//ROWS
