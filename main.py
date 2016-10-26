import pygame
from pygame.locals import *

from Sidebar import Sidebar
from ToggleButton import ToggleButton
from ContextMenu import ContextMenu
from ContextMenuEntry import ContextMenuEntry
from Graph import Graph
from Button import Button

screen_width = 1280
screen_height = 720
main_surface = pygame.display.set_mode((screen_width, screen_height), HWSURFACE)

mouse = None

my_sidebar = Sidebar((250, screen_height), pygame.Color('#30556c'), pygame.Color('#7c7a7a'))
my_toggle_button = ToggleButton((screen_width - 200, 30), (200, 0, 0), (0, 200, 0), 'degrees', 'radians')

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
        elif event.type == KEYDOWN:
            pass

    main_surface.fill(pygame.Color('#ebebeb'))
    my_sidebar.x += my_sidebar.speed
    if my_sidebar.speed < 0:
        my_sidebar.speed += my_sidebar.increment
    elif my_sidebar.speed > 0:
        my_sidebar.speed -= my_sidebar.increment

    mouse_pos = pygame.mouse.get_pos()
    if not my_sidebar.popped_out and mouse_pos[0] < 10:
        my_sidebar.pop_out()
    elif my_sidebar.popped_out and mouse_pos[0] > my_sidebar.size[0]:
        my_sidebar.pop_in()

    if my_sidebar.x < -my_sidebar.size[0]:
        my_sidebar.speed = 0
        my_sidebar.x = -my_sidebar.size[0]
    elif my_sidebar.x > 0:
        my_sidebar.speed = 0
        my_sidebar.x = 0

    my_toggle_button.slider_x += my_toggle_button.speed
    if my_toggle_button.speed < 0:
        my_toggle_button.speed += my_toggle_button.increment
    elif my_toggle_button.speed > 0:
        my_toggle_button.speed -= my_toggle_button.increment

    if my_toggle_button.slider_x < 0:
        my_toggle_button.speed = 0
        my_toggle_button.slider_x = 0
    elif my_toggle_button.slider_x >= my_toggle_button.side_size:
        my_toggle_button.speed = 0
        my_toggle_button.slider_x = my_toggle_button.side_size

    mouse_bool = my_toggle_button.is_moused_over()
    if mouse_bool and mouse == MOUSEBUTTONDOWN:
        if my_toggle_button.toggled:
            my_toggle_button.turn_off()
        else:
            my_toggle_button.turn_on()

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

    my_toggle_button.redraw_surface()

    my_graph.draw_grid()

    main_surface.blit(my_graph, (0, 0))
    main_surface.blit(my_toggle_button, my_toggle_button.pos)
    main_surface.blit(my_sidebar, (my_sidebar.x, 0))

    context.set_surface()
    main_surface.blit(context, context.pos)

    my_button.set_surface(mouse)
    main_surface.blit(my_button, my_button.pos)

    pygame.display.update()
    mouse = None
pygame.quit()
