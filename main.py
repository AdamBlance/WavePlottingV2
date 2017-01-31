import pygame

from Sidebar import Sidebar
from ToggleButton import ToggleButton
from EventManager import EventManager
from FunctionBox import FunctionBox
from Graph import Graph

from sympy import *
x = symbols('x')

screen_width = 1280
screen_height = 720
main_surface = pygame.display.set_mode((screen_width, screen_height))

event_manager = EventManager()

my_sidebar = Sidebar((300, screen_height), pygame.Color('#30556c'), pygame.Color('#7c7a7a'))
# my_function_box = FunctionBox(event_manager, (0, 100), (300, 75), my_sidebar)
my_toggle_button = ToggleButton(event_manager, (95, 25), [screen_width - 220, 30], 'degrees', 'radians')
my_graph = Graph(event_manager, (screen_width, screen_height))

clock = pygame.time.Clock()
while not event_manager.has_quit:

    clock.tick(60)
    event_manager.update()

    # my_function_box.update()
    my_toggle_button.update()
    my_sidebar.update()
    my_graph.update()

    main_surface.blit(my_graph, (0, 0))

    # my_sidebar.blit(my_function_box, my_function_box.pos)
    main_surface.blit(my_sidebar, my_sidebar.pos)
    main_surface.blit(my_toggle_button, my_toggle_button.pos)
    pygame.display.update()

pygame.quit()
