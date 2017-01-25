import pygame
from pygame.locals import *
from sympy import *
from math import pi


class Graph(pygame.Surface):
    function_resolution = 3  # int > 0

    def __init__(self, size):
        super().__init__(size, SRCALPHA)

        self.all_functions = []

        self.size = size
        self.segment_size = 10

        self.screen_ratio = self.size[1]/self.size[0]

        self.x_min = -2*pi
        self.x_max = 2*pi
        self.y_min = -9/16*2*pi
        self.y_max = 9/16*2*pi

    def screen_to_graph_x(self, x_coord):
        x = (x_coord / self.size[0]) * (self.x_max - self.x_min) + self.x_min
        return x

    def screen_to_graph_y(self, y_coord):
        y = ((y_coord - self.size[1]) / -self.size[1]) * (self.y_max - self.y_min) + self.y_min
        return y

    def graph_to_screen_x(self, x_coord):
        x = ((x_coord - self.x_min) / (self.x_max - self.x_min)) * self.size[0]
        return x

    def graph_to_screen_y(self, y_coord):
        y = ((y_coord - self.y_max) / (self.y_min - self.y_max)) * self.size[1]
        return y

    def draw_function(self, function):
        x = symbols('x')
        point_array = []
        for pixel in range(0, self.size[0], self.function_resolution):
            print(pixel)
            x_coord = self.screen_to_graph_x(pixel)
            y_coord = self.graph_to_screen_y(function.subs(x, x_coord).evalf())

            point_array.append((pixel, y_coord))
        pygame.draw.aalines(self, pygame.Color('red'), False, point_array)
