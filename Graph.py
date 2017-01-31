import pygame
from pygame.locals import *
from sympy import *
from FunctionBox import FunctionBox


class Graph(pygame.Surface):
    function_resolution = 1  # int > 0

    def __init__(self, event_manager, size):
        super().__init__(size, SRCALPHA)

        self.event_manager = event_manager

        self.size = size
        self.segment_size = 10

        self.screen_ratio = self.size[1]/self.size[0]

        pie = float(pi)
        self.x_min = -2*pie
        self.x_max = 2*pie
        self.y_min = -9/16*2*pie
        self.y_max = 9/16*2*pie

        self.x = symbols('x')

    def shift_screen(self, x, y):
        pass

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

        point_array = []
        subbable = lambdify(self.x, function, 'numpy')
        for pixel in range(0, self.size[0], self.function_resolution):
            x_coord = self.screen_to_graph_x(pixel)
            subbed = subbable(x_coord)
            y_coord = self.graph_to_screen_y(subbed)
            point_array.append((pixel, y_coord))
        pygame.draw.lines(self, pygame.Color('red'), False, point_array)

    def update(self):
        self.fill(pygame.Color('#ebebeb'))

        x_increment = abs(self.x_max - self.x_min)/self.size[0]
        y_increment = abs(self.y_max - self.y_min)/self.size[1]

        mouse_rel = pygame.mouse.get_rel()
        if self.event_manager.lmb_held:
            mouse_x = mouse_rel[0]*x_increment*-1
            mouse_y = mouse_rel[1]*y_increment
            self.x_min += mouse_x
            self.x_max += mouse_x
            self.y_min += mouse_y
            self.y_max += mouse_y

        x_indent = abs(self.x_max - self.x_min) / 10
        y_indent = abs(self.y_max - self.y_min) / 10

        if self.event_manager.scrolled_up:
            self.x_min += x_indent
            self.x_max -= x_indent
            self.y_min += y_indent
            self.y_max -= y_indent
        elif self.event_manager.scrolled_down:
            self.x_min -= x_indent
            self.x_max += x_indent
            self.y_min -= y_indent
            self.y_max += y_indent

        self.draw_function(sin(self.x) + cos(4*self.x))
