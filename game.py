import pygame

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
        self.scale = board.scale

    def place_snake(self):
        self.x_pos = board.width/board.scale//2
        self.y_pos = board.height/board.scale//2
        self.length = 0
        self.tail = []
        self.x_speed = 0
        self.y_speed = 0

    def draw(self):
        # head
        pygame.draw.rect(screen, [0, 255, 0],
                [self.x_pos*self.scale, self.y_pos*self.scale,
                    self.scale, self.scale], 0)
        # tail
        for element in self.tail:
            pygame.draw.rect(screen, [0, 255, 0],
                    [element[0]*self.scale, element[1]*self.scale,
                        self.scale, self.scale], 0)

    def check_collision(self):
        border_collision = self.x_pos >= board.width//board.scale\
                or self.x_pos < 0\
                or self.y_pos >= board.height//board.scale\
                or self.y_pos < 0
        body_collision = False
        for element in self.tail:
            if self.x_pos == element[0] or self.y_pos == element[1]:
                body_collision = True
        if border_collision or body_collision:
            self.place_snake()

    def slither(self):
        self.x_pos += self.x_speed
        self.y_pos += self.y_speed
        self.tail.append([self.x_pos, self.y_pos])
        self.tail.pop(0)


board = Board(800, 800, 20)
snake = Snake(board)
snake.place_snake()

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
    snake.check_collision()

    # draw loop
    screen.fill([0,0,0])

    snake.draw()

    pygame.display.flip()

    clock.tick(10)

pygame.quit()
