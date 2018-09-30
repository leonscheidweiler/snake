import pygame

class Snake:
    board = None
    x_pos = 0
    y_pos = 0
    x_speed = 0
    y_speed = 0
    tail = []
    color = [0, 255, 0]
    screen = None

    def __init__(self, board):
        self.board = board

    def place(self):
        self.x_pos = self.board.width//self.board.scale//2 + self.board.x_pos
        self.y_pos = self.board.height//self.board.scale//2 + self.board.y_pos
        self.tail = []
        self.x_speed = 0
        self.y_speed = 0

    def collided(self):
        border_collision = self.x_pos >= self.board.width//self.board.scale + self.board.x_pos\
                or self.x_pos < 0 + self.board.x_pos\
                or self.y_pos >= self.board.height//self.board.scale + self.board.y_pos\
                or self.y_pos < 0 + self.board.y_pos
        body_collision = False
        for element in self.tail:
            if self.x_pos == element[0] and self.y_pos == element[1]:
                body_collision = True
        return border_collision or body_collision

    def slither(self):
        self.tail.append([self.x_pos, self.y_pos])
        self.tail.pop(0)
        self.x_pos += self.x_speed
        self.y_pos += self.y_speed

    def devour(self):
        self.tail.append([self.x_pos, self.y_pos])

    def draw(self):
        # head
        pygame.draw.rect(self.screen, self.color,
                [self.x_pos*self.board.scale, self.y_pos*self.board.scale,
                    self.board.scale, self.board.scale], 0)
        # tail
        for element in self.tail:
            pygame.draw.rect(self.screen, self.color,
                    [element[0]*self.board.scale, element[1]*self.board.scale,
                        self.board.scale, self.board.scale], 0)
