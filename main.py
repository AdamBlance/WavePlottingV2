import pygame
from pygame.locals import *

from Sidebar import Sidebar
from ToggleButton import ToggleButton
from ContextMenu import ContextMenu
from ContextMenuEntry import ContextMenuEntry
from Graph import Graph
from Button import Button

# todo: Write a state machine class for the event queue
# todo: Write a class for clickable objects to prevent duplicate code

screen_width = 1280
screen_height = 720
main_surface = pygame.display.set_mode((screen_width, screen_height), HWSURFACE)

mouse = None

my_sidebar = Sidebar((250, screen_height), pygame.Color('#30556c'), pygame.Color('#7c7a7a'))
my_toggle_button = ToggleButton([screen_width - 200, 30], 'degrees', 'radians')

back = ContextMenuEntry('Back', print, 'Back')
forward = ContextMenuEntry('Forward', print, 'Forward')
reload = ContextMenuEntry('Reload', print, 'Reload')
view_source = ContextMenuEntry('View Source', print, 'View Source')
fill = ContextMenuEntry('Fill', main_surface.fill, (255, 255, 0))

context = ContextMenu((200, 200), [back, forward, reload, view_source, fill])

my_graph = Graph((screen_width, screen_height))

my_button = Button((500, 200), pygame.Color(100, 100, 100), 'Sample Text', print, 'Sample Text')

clock = pygame.time.Clock()
temp = False
running = True
while running:

    # todo: Move all of this fluff into the relevant classes

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONUP or event.type == MOUSEBUTTONDOWN:
            mouse = event.type

    main_surface.fill(pygame.Color('#ebebeb'))

    for entry in context.entries:
        mouse_bool0 = context.is_moused_over(entry)
        if mouse_bool0:
            if mouse == MOUSEBUTTONDOWN:
                entry.depressed = True
            elif mouse == MOUSEBUTTONUP and entry.depressed:
                entry.depressed = False
                entry.call_function()
        else:
            entry.depressed = False

    my_toggle_button.update()

    my_graph.draw_grid()

    my_sidebar.update()

    main_surface.blit(my_graph, (0, 0))
    main_surface.blit(my_sidebar, my_sidebar.pos)

    context.set_surface()
    main_surface.blit(context, context.pos)

    my_button.set_surface(mouse)
    main_surface.blit(my_button, my_button.pos)

    main_surface.blit(my_toggle_button, my_toggle_button.pos)
    pygame.display.update()

    mouse = None
pygame.quit()
