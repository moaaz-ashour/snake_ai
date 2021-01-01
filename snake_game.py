import pygame
import random

# needed to initialize all modules correctly
pygame.init()

class SnakeGame:
    def __init__(self, width=640, height=380): # default width and height
        self.width = width
        self.height = height

        # init window/display with width and height (create a display Surface)
        self.display = pygame.display.set_mode((self.width, self.height))
        # control speed of the game
        self.clock = pygame.time.Clock()

        
if __name__ == '__main__':
    # create snake game
    game = SnakeGame()