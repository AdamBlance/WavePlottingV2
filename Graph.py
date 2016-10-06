import pygame
from pygame.locals import *


class Graph(pygame.Surface):
    def __init__(self, size):
        super().__init__(size, SRCALPHA)

        self.size = size
        self.segment_size = 10
        self.origin = (int(size[0]/2), int(size[1]/2))

    def draw_grid(self):
        pygame.draw.line(self, (0, 175, 0), (self.origin[0], 0), (self.origin[0], self.size[1]), 3)
        pygame.draw.line(self, (175, 0, 0), (0, self.origin[1]), (self.size[0], self.origin[1]), 3)
        pygame.draw.circle(self, (0, 0, 0), self.origin, 2)

