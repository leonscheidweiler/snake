import pygame

class Board:
    x_pos  = 0
    y_pos  = 0
    width  = 0
    height = 0
    scale  = 0
    color = [20, 20, 20]
    screen = None

    def __init__(self, x_pos, y_pos, width, height, scale):
        self.x_pos = x_pos
        self_y_pos = y_pos
        self.width = width
        self.height = height
        self.scale = scale

    def draw(self):
        print('nothing yet')
