import pygame
import random

class Food:
    board = None
    snake = None
    x_pos = 0
    y_pos = 0
    color = [255, 0, 0]
    screen = None

    def __init__(self, board, snake):
        self.board = board
        self.snake = snake

    def place(self):
        while True:
            self.x_pos = random.randint(0, self.board.width//self.board.scale-1) + self.board.x_pos
            self.y_pos = random.randint(0, self.board.height//self.board.scale-1) + self.board.y_pos
            for element in self.snake.tail:
                if element[0]==self.x_pos and element[1]==self.y_pos:
                    continue
            break

    def eaten(self):
        return self.snake.x_pos == self.x_pos and self.snake.y_pos == self.y_pos

    def draw(self):
        pygame.draw.rect(self.screen, self.color,
                [self.x_pos*self.board.scale, self.y_pos*self.board.scale,
                    self.board.scale, self.board.scale], 0)
