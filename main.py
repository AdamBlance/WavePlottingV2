import pygame

from Sidebar import Sidebar
from ToggleButton import ToggleButton
from ContextMenu import ContextMenu
from ContextMenuEntry import ContextMenuEntry
from Graph import Graph
from Button import Button
from EventManager import EventManager

# todo: Write a state machine class for the event queue
# todo: Write a class for clickable objects to prevent duplicate code

screen_width = 1280
screen_height = 720
main_surface = pygame.display.set_mode((screen_width, screen_height))

mouse = None

event_manager = EventManager()

my_sidebar = Sidebar((250, screen_height), pygame.Color('#30556c'), pygame.Color('#7c7a7a'))
my_toggle_button = ToggleButton(event_manager, [screen_width - 200, 30], 'degrees', 'radians')

back = ContextMenuEntry('Back', print, 'Back')
forward = ContextMenuEntry('Forward', print, 'Forward')
reload = ContextMenuEntry('Reload', print, 'Reload')
view_source = ContextMenuEntry('View Source', print, 'View Source')
fill = ContextMenuEntry('Fill', main_surface.fill, (255, 255, 0))

context = ContextMenu(event_manager, (200, 200), [back, forward, reload, view_source, fill])

my_graph = Graph((screen_width, screen_height))

my_button = Button(event_manager, (500, 200), pygame.Color(100, 100, 100), 'Sample Text', print, 'Sample Text')

clock = pygame.time.Clock()
temp = False
running = True
while not event_manager.has_quit:

    clock.tick(60)

    event_manager.update()

    my_toggle_button.update()
    my_sidebar.update()
    context.update()
    my_button.update()

    main_surface.fill(pygame.Color('#ebebeb'))

    main_surface.blit(my_graph, (0, 0))
    main_surface.blit(my_sidebar, my_sidebar.pos)
    main_surface.blit(context, context.pos)

    main_surface.blit(my_button, my_button.pos)
    main_surface.blit(my_toggle_button, my_toggle_button.pos)
    pygame.display.update()

    mouse = None
pygame.quit()
