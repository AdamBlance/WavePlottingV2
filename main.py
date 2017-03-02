import pygame
import pygame.freetype

from Sidebar import Sidebar
from ToggleButton import ToggleButton
from EventManager import EventManager
from Graph import Graph
from TextContainer import TextContainer

from sympy import *
x = symbols('x')

pygame.freetype.init()

screen_width = 1280
screen_height = 720
main_surface = pygame.display.set_mode((screen_width, screen_height))

event_manager = EventManager()

my_sidebar = Sidebar((300, screen_height), pygame.Color('#30556c'), pygame.Color('#7c7a7a'))
my_toggle_button = ToggleButton(event_manager, (95, 25), [screen_width - 220, 30], 'degrees', 'radians')
my_graph = Graph(event_manager, (10, 0), (screen_width, screen_height))

my_text_container = TextContainer(event_manager, (400, 250), pygame.Color('green'))

text_selector = (
'    XXXXXXX     ',
'    X..X..X     ',
'    XXX.XXX     ',
'      X.X       ',
'      X.X       ',
'      X.X       ',
'      X.X       ',
'      X.X       ',
'      X.X       ',
'      X.X       ',
'      X.X       ',
'      X.X       ',
'      X.X       ',
'    XXX.XXX     ',
'    X..X..X     ',
'    XXXXXXX     '
)

normal_cursor = (
'X                       ',
'XX                      ',
'X.X                     ',
'X..X                    ',
'X...X                   ',
'X....X                  ',
'X.....X                 ',
'X......X                ',
'X.......X               ',
'X........X              ',
'X.........X             ',
'X..........X            ',
'X...........X           ',
'X............X          ',
'X.............X         ',
'X........XXXXXXX        ',
'X........X              ',
'X....X...X              ',
'X...X X...X             ',
'X..X  X...X             ',
'X.X    X...X            ',
'XX     X...X            ',
'X       X..X            ',
'        XXXX            '
)

compiled = pygame.cursors.compile(text_selector, black='X', white='.', xor='o')
pygame.mouse.set_cursor((16, 16), (8, 8), compiled[0], compiled[1])

while not event_manager.has_quit:

    event_manager.clock.tick(60)
    event_manager.update()

    if my_toggle_button.was_clicked:
        my_graph.toggle_degrees()

    my_toggle_button.update()
    my_sidebar.update()
    my_graph.update()

    my_text_container.update()

    main_surface.blit(my_graph, my_graph.pos)
    main_surface.blit(my_toggle_button, my_toggle_button.pos)
    main_surface.blit(my_sidebar, my_sidebar.pos)
    main_surface.blit(my_text_container, my_text_container.pos)

    pygame.display.update()

pygame.quit()
