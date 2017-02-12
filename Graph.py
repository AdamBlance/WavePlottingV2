import pygame
from pygame.locals import *
from sympy import *


class Graph(pygame.Surface):
    function_resolution = 1  # int > 0

    def __init__(self, event_manager, size):
        super().__init__(size, SRCALPHA)

        self.event_manager = event_manager

        self.size = size

        self.screen_ratio = self.size[1]/self.size[0]
        pie = float(pi)
        self.x_min = -2*pie
        self.x_max = 2*pie
        self.y_min = -9/16*2*pie
        self.y_max = 9/16*2*pie

        self.line_spacing = pie
        self.current_x_lines = None
        self.current_y_lines = None

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
        return int(x)

    def graph_to_screen_y(self, y_coord):
        y = ((y_coord - self.y_max) / (self.y_min - self.y_max)) * self.size[1]
        return int(y)

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

        if self.current_x_lines is not None:
            if self.current_x_lines > 16:
                self.line_spacing *= 2
            elif self.current_x_lines < 8:
                self.line_spacing /= 2
        self.current_x_lines = round((self.x_max-self.x_min)/self.line_spacing)
        self.current_y_lines = round((self.y_max-self.y_min)/self.line_spacing)
        last_x_line = int(self.x_min/self.line_spacing)*self.line_spacing
        last_y_line = int(self.y_min/self.line_spacing)*self.line_spacing

        for i in range(self.current_x_lines + 1):
            x_point = self.graph_to_screen_x(last_x_line + i*self.line_spacing)
            pygame.draw.line(self, pygame.Color('grey'), (x_point, 0), (x_point, self.size[1]))
            y_point = self.graph_to_screen_y(last_y_line + i*self.line_spacing)
            pygame.draw.line(self, pygame.Color('grey'), (0, y_point), (self.size[0], y_point))

        x_range = abs(self.x_max-self.x_min)
        y_range = abs(self.x_max-self.x_min)

        x_increment = x_range/self.size[0]
        y_increment = y_range/self.size[1]

        mouse_rel = pygame.mouse.get_rel()
        if self.event_manager.lmb_held:
            mouse_x = mouse_rel[0]*x_increment*-1
            mouse_y = mouse_rel[1]*y_increment
            self.x_min += mouse_x
            self.x_max += mouse_x
            self.y_min += mouse_y
            self.y_max += mouse_y

        if self.event_manager.scrolled_up or K_UP in self.event_manager.keys_pressed:
            self.x_min *= 0.9
            self.x_max *= 0.9
            self.y_min *= 0.9
            self.y_max *= 0.9

        elif self.event_manager.scrolled_down or K_DOWN in self.event_manager.keys_pressed:
            self.x_min *= 1.1
            self.x_max *= 1.1
            self.y_min *= 1.1
            self.y_max *= 1.1

        origin = (self.graph_to_screen_x(0), self.graph_to_screen_y(0))
        if self.x_min < 0 < self.x_max and self.y_min < 0 < self.y_max:
            pygame.draw.circle(self, pygame.Color('blue'), origin, 5)

        self.draw_function(sin(self.x))
