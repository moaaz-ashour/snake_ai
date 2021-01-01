import pygame
import random
from enum import Enum
from collections import namedtuple

# needed to initialize all modules correctly
pygame.init()

class Direction(Enum):
    # CONSTANTS enumeration members
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4


# create a Point object and accessing x and y coordinates
Point = namedtuple('Point', ['x', 'y'])

class SnakeGame:
    def __init__(self, width=640, height=380): # default width and height
        self.width = width
        self.height = height

        # init window/display with width and height (create a display Surface)
        self.display = pygame.display.set_mode((self.width, self.height))
        # control speed of the game
        self.clock = pygame.time.Clock()

        # init game state:
        # 1. initial direction:
        self.direction = Direction.RIGHT

        # 2. initial snake head: store coordinates of head
        self.head = Point(self.width/2, self.height/2) # > Point(x=320.0, y=190.0)
        
            
if __name__ == '__main__':
    # create snake game
    game = SnakeGame()