import pygame
import random

from board import *
from snake import *
from food import *

pygame.init()
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

board = Board(0, 0, 500, 700, 20)
snake = Snake(board)
food = Food(board, snake)

screen = pygame.display.set_mode([500, 700])
snake.screen = screen
food.screen = screen
board.screen = screen

snake.place()
food.place()

game_running = True

while game_running:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and prev_y_speed != -1:
                snake.x_speed = 0.
                snake.y_speed = 1.
            if event.key == pygame.K_UP and prev_y_speed != 1:
                snake.x_speed = 0.
                snake.y_speed = -1.
            if event.key == pygame.K_LEFT and prev_x_speed != 1:
                snake.x_speed = -1.
                snake.y_speed = 0.
            if event.key == pygame.K_RIGHT and prev_x_speed != -1:
                snake.x_speed = 1.
                snake.y_speed = 0.
    
    # game loop
    snake.slither()

    if snake.collided():
        snake.place()

    if food.eaten():
        snake.devour()
        food.place()

    prev_x_speed = snake.x_speed
    prev_y_speed = snake.y_speed

    # draw loop
    screen.fill([0,0,0])

    board.draw()
    snake.draw()
    food.draw()

    pygame.display.flip()

    clock.tick(board.height/board.scale//4)

pygame.quit()
