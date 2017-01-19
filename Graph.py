import pygame
from pygame.locals import *
from sympy import *
from math import pi as float_pi


class Graph(pygame.Surface):
    functions = []
    function_resolution = 1  # From 0 to 1

    def __init__(self, size):
        super().__init__(size, SRCALPHA)

        self.size = size
        self.segment_size = 10

        self.screen_ratio = self.size[1]/self.size[0]

        self.x_min = 0
        self.x_max = 2*float_pi

    def draw_function(self, function):
        pass