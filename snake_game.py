import pygame
import random
from enum import Enum
from collections import namedtuple

# needed to initialize all modules correctly
pygame.init()

# defining a font for the score
# you can also use Font('arial.ttf', 25) which is much faster.
font = pygame.font.SysFont('arial', 25) 
class Direction(Enum):
    # CONSTANTS enumeration members
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4


# create a Point object and accessing x and y coordinates
Point = namedtuple('Point', ['x', 'y'])

BLOCK_SIZE = 20
SPEED = 20

# RGB colors as pygame colos
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE1 = (0, 0, 255)
BLACK = (0, 0, 0)

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
        
        # keep track of score:
        self.score = 0

        # init food
        self.food = None
        # randomly place food on display
        self._place_food()
        
                
    def _place_food(self):
        # random positions of snake food which are multiple of BLOCK_SIZE
        x = random.randint(0, (self.width-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        y = random.randint(0, (self.height-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        # create food Point 
        self.food = Point(x, y)
        # recursive call: make sure the food is not inside the snake
        if self.food in self.snake:
            self._place_food()

    # play steps
    def play_steps(self):
        # 1. collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # quit python program
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN
        
        # 2. move snake: get new coordinates for the head and update it
        self._move(self.direction)
        self.snake.insert(0, self.head)
        
        
        # 3. update UI and controlling the Clock speed
        self._update_ui()
        self.clock.tick(SPEED)
        game_over = False
        return game_over, self.score

    # updating UI
    def _update_ui(self):
        # 1. fill display with black color
        self.display.fill(BLACK)
        # 2. draw snake
        for pt in self.snake:
            # Outer: rectangles with blue color with its size as BLOCK_SIZE (width and height)
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            # Inner: rectangles but smaller and white color
            pygame.draw.rect(self.display, WHITE, pygame.Rect(pt.x+4, pt.y+4, BLOCK_SIZE -8, BLOCK_SIZE-8))   
        
        # 3. draw the food
        # pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))
        test = pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))
        print(test)
        # 4. draw score on upper left corner (You need a font)
        text = font.render("Score: " + str(self.score), True, WHITE)
        # 5. display Surface on screen   
        self.display.blit(text, [0,0])
        # 6. update the full display Surface: Without this you won't see any changes
        pygame.display.flip()

    # gets new coordinates for the head and updates it   
    def _move(self, direction):
        x = self.head.x
        y = self.head.y
        if direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif direction == Direction.UP:
            y -= BLOCK_SIZE
        # after we have the new coordinates, we can create the head (update it)
        self.head = Point(x, y)
            
        
if __name__ == '__main__':
    # create snake game
    game = SnakeGame()
    
    # game loop
    while True:
        game_over, score = game.play_steps()
        if game_over == True:
            break
    print(f'final score: {score}')