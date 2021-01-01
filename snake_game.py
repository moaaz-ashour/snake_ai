import pygame
import random

# needed to initialize all modules correctly
pygame.init()

class SnakeGame:
    def __init__(self, width=640, height=380): # default width and height
        self.width = width
        self.height = height

        # init display with width and height
        self.display = pygame.display.set_mode(self.width, self.height)



if __name__ == '__main__':
    # create a snake game
    game = SnakeGame()