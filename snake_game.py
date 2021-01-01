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

BLOCK_SIZE = 20
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
        
        # 3. initial snake position: store 3 coordinates:
        # > Point(x=320.0, y=190.0)
        # > Point(x=300.0, y=190.0)
        # > Point(x=280.0, y=190.0)
        self.snake = [self.head,
                      Point(self.head.x-BLOCK_SIZE, self.head.y), 
                      Point(self.head.x-(2*BLOCK_SIZE), self.head.y)
                      ]
        
        # initial food
        self.food = None
        # randomly place food on display
        self._place_food()
        
        # keep track of score:
        self.score = 0
                
    def _place_food(self):
        # random positions of snake food which are multiple of BLOCK_SIZE
        x = random.randint(0, (self.width-BLOCK_SIZE//BLOCK_SIZE))*BLOCK_SIZE
        y = random.randint(0, (self.height-BLOCK_SIZE//BLOCK_SIZE))*BLOCK_SIZE
        # create food Point 
        self.food = Point(x, y)
        # recursive call: make sure the food is not inside the snake
        if self.food in self.snake:
            self._place_food()
            
if __name__ == '__main__':
    # create snake game
    game = SnakeGame()