from GUIObject import GUIObject
import pygame
from pygame.locals import *
from sympy import *
from math import degrees
from fractions import Fraction


class Graph(GUIObject):
    function_resolution = 1  # int > 0

    def __init__(self, event_manager, pos, size):
        super().__init__(pos, size)

        self.event_manager = event_manager

        self.size = size

        pie = float(pi)
        ratio = self.size[1]/self.size[0]
        self.x_min = -2*pie
        self.x_max = 2*pie
        self.y_min = -ratio*2*pie
        self.y_max = ratio*2*pie

        self.is_radians = True

        self.x_line_spacing = 8*pie
        self.y_line_spacing = 1
        self.current_x_lines = None
        self.current_y_lines = None
        self.x_lines_offset = False
        self.y_lines_offset = False

        self.x = symbols('x')

    def toggle_degrees(self):
        if self.is_radians:
            self.is_radians = False
        else:
            self.is_radians = True

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

    @staticmethod
    def limit_lines(current_lines, spacing):
        new_space = spacing
        if current_lines is not None:
            if current_lines > 16:
                new_space *= 2
            elif current_lines < 8:
                new_space /= 2
        return new_space

    def draw_gridlines(self):

        self.current_y_lines = round((self.y_max-self.y_min)/self.y_line_spacing)
        self.y_line_spacing = self.limit_lines(self.current_y_lines, self.y_line_spacing)
        last_y_line = int(self.y_min/self.y_line_spacing)*self.y_line_spacing

        for i in range(self.current_y_lines + 2):
            graph_y = last_y_line + i*self.y_line_spacing
            y_point = self.graph_to_screen_y(graph_y)
            y_numbers = graph_y

            origin_x = self.graph_to_screen_x(0)
            text_size = self.small_main_font.size(str(y_numbers) + '0')[0] + 5
            if origin_x < 3:
                y_text_pos = 3
                self.y_lines_offset = True
            elif origin_x > self.size[0]-text_size:
                y_text_pos = self.size[0]-text_size
                self.y_lines_offset = True
            else:
                y_text_pos = origin_x
                self.y_lines_offset = False

            if not (self.x_lines_offset and graph_y == 0):
                rendered_text = self.small_main_font.render(str(round(y_numbers, 3)), True, pygame.Color('black'))
                self.blit(rendered_text, (y_text_pos, y_point))
            pygame.draw.line(self, pygame.Color('grey'), (0, y_point), (self.size[0], y_point))

        self.current_x_lines = round((self.x_max-self.x_min)/self.x_line_spacing)
        self.x_line_spacing = self.limit_lines(self.current_x_lines, self.x_line_spacing)
        last_x_line = int(self.x_min/self.x_line_spacing)*self.x_line_spacing

        for i in range(-1, self.current_x_lines + 1):
            graph_x = last_x_line + i*self.x_line_spacing
            x_point = self.graph_to_screen_x(graph_x)
            if not self.is_radians:
                x_numbers = degrees(graph_x)
            else:
                x_numbers = graph_x

            origin_y = self.graph_to_screen_y(0)
            if origin_y < 0:
                x_text_pos = 0
                self.x_lines_offset = True
            elif origin_y > self.size[1]-15:
                x_text_pos = self.size[1]-15
                self.x_lines_offset = True
            else:
                x_text_pos = origin_y
                self.x_lines_offset = False

            # TODO: Scientific notation

            unit_string = '0.0'
            if not (self.y_lines_offset and graph_x == 0):
                if x_numbers != 0:
                    if self.is_radians:
                        coefficient = Fraction(round(x_numbers/float(pi), 8))
                        unit_string = ('%s|%s\u03C0' % (coefficient.numerator, coefficient.denominator)).replace('|1', '')
                    else:
                        unit_string = str(x_numbers)

                rendered_text = self.small_main_font.render(unit_string, True, pygame.Color('black'))
                self.blit(rendered_text, (x_point, x_text_pos))
            pygame.draw.line(self, pygame.Color('grey'), (x_point, 0), (x_point, self.size[1]))

    def update(self):

        self.fill(pygame.Color('#ebebeb'))

        x_range = abs(self.x_max-self.x_min)
        y_range = abs(self.y_max-self.y_min)
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

        # TODO: Fix zooming so it doesn't zoom to centre

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

        self.draw_gridlines()
        self.draw_function(sin(self.x))
        origin = (self.graph_to_screen_x(0), self.graph_to_screen_y(0))
        if (-20 < origin[0] < self.size[0]+20) and (-20 < origin[1] < self.size[1]+20):
            pygame.draw.circle(self, pygame.Color('blue'), origin, 5)
