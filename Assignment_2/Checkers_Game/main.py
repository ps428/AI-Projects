import min_max
import values
import pygame
import time

window = pygame.display.set_mode((values.WIDTH+values.OPTIONS_PANEL_SIZE, values.HEIGHT))
pygame.display.set_caption("Checker's Menu Driven")

# calling the ai moves for a basic game type

min_max.ai_play()