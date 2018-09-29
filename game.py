import pygame

import random

class Board:
    width = 0
    height = 0
    scale = 0

    def __init__(self, width, height, scale):
        self.width = width
        self.height = height
        self.scale = scale

class Snake:
    board = None
    x_pos = 0
    y_pos = 0
    x_speed = 0
    y_speed = 0
    length = 0
    tail = []

    def __init__(self, board):
        self.board = board

    def place(self):
        self.x_pos = board.width/board.scale//2
        self.y_pos = board.height/board.scale//2
        self.tail = []
        self.x_speed = 0
        self.y_speed = 0

    def draw(self):
        # head
        pygame.draw.rect(screen, [0, 255, 0],
                [self.x_pos*board.scale, self.y_pos*board.scale,
                    board.scale, board.scale], 0)
        # tail
        for element in self.tail:
            pygame.draw.rect(screen, [0, 255, 0],
                    [element[0]*board.scale, element[1]*board.scale,
                        board.scale, board.scale], 0)

    def collided(self):
        border_collision = self.x_pos >= board.width//board.scale\
                or self.x_pos < 0\
                or self.y_pos >= board.height//board.scale\
                or self.y_pos < 0
        body_collision = False
        for element in self.tail:
            if self.x_pos == element[0] or self.y_pos == element[1]:
                body_collision = True
        return border_collision or body_collision

    def slither(self):
        self.tail.append([self.x_pos, self.y_pos])
        self.tail.pop(0)
        self.x_pos += self.x_speed
        self.y_pos += self.y_speed

    def devour(self):
        self.tail.append([self.x_pos, self.y_pos])

class Apple:
    board = None
    snake = None
    x_pos = 0
    y_pos = 0

    def __init__(self, board, snake):
        self.board = board
        self.snake = snake

    def place(self):
        self.x_pos = random.randint(0, board.width//board.scale-1)
        self.y_pos = random.randint(0, board.height//board.scale-1)

    def eaten(self):
        return snake.x_pos == self.x_pos and snake.y_pos == self.y_pos

    def draw(self):
        pygame.draw.rect(screen, [255, 0, 0],
                [self.x_pos*board.scale, self.y_pos*board.scale,
                    board.scale, board.scale], 0)

board = Board(800, 800, 20)
snake = Snake(board)
apple = Apple(board, snake)

snake.place()
apple.place()

game_running = True

screen = pygame.display.set_mode([board.width, board.height])

pygame.init()
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

while game_running:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and not snake.y_speed < 0:
                snake.x_speed = 0
                snake.y_speed = 1
            if event.key == pygame.K_UP and not snake.y_speed > 0:
                snake.x_speed = 0
                snake.y_speed = -1
            if event.key == pygame.K_LEFT and not snake.x_speed > 0:
                snake.x_speed = -1
                snake.y_speed = 0
            if event.key == pygame.K_RIGHT and not snake.x_speed < 0:
                snake.x_speed = 1
                snake.y_speed = 0
    
    # game loop
    snake.slither()

    if apple.eaten():
        snake.devour()
        apple.place()

    if snake.collided():
        snake.place()

    # draw loop
    screen.fill([0,0,0])

    snake.draw()
    apple.draw()

    pygame.display.flip()

    clock.tick(10)

pygame.quit()
