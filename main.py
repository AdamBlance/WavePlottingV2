from EventManager import EventManager
from Graph import Graph
from Sidebar import Sidebar
from Button import Button
from ToggleButton import ToggleButton
from TextContainer import TextContainer
import pygame
import pygame.freetype

pygame.init()

screen_width = 1280
screen_height = 720
main_surface = pygame.display.set_mode((screen_width, screen_height))

text_container_height = 80
padding = 20
max_cont = (screen_height // (text_container_height + padding)) - 2


def create_new_text_container():
    if len(TextContainer.all_text_entries)-1 != max_cont:
        TextContainer(event_manager, 30, (300, text_container_height))

event_manager = EventManager()

text_container = TextContainer

graph = Graph(event_manager, (0, 0), (screen_width, screen_height))
sidebar = Sidebar((300, screen_height), pygame.Color('#3a577b'), pygame.Color('#4d4d4d'))
toggle_button = ToggleButton(event_manager, (95, 25), [screen_width - 220, 30], 'degrees', 'radians')

new_expr = Button(event_manager, (25, screen_height - 60), pygame.Color(0, 200, 0), 'ADD NEW', create_new_text_container, size=(90, 35), gui_object_blitted_to=sidebar)

while not event_manager.has_quit:

    event_manager.clock.tick(60)
    event_manager.update()

    if toggle_button.was_clicked:
        graph.toggle_degrees()

    mouse_pos = pygame.mouse.get_pos()
    if event_manager.lmb_down and 0 < mouse_pos[0] < 300:
        bounds = mouse_pos[1] // (text_container_height + padding)
        if bounds < len(TextContainer.all_text_entries):
            for item in TextContainer.all_text_entries:
                item.is_current = False
            TextContainer.all_text_entries[bounds].is_current = True

    sidebar.update()

    try:
        graph.update()
    except TypeError:
        print(':(')

    toggle_button.update()
    new_expr.update()

    main_surface.blit(graph, graph.pos)

    main_surface.blit(sidebar, sidebar.pos)

    for i in range(len(TextContainer.all_text_entries)):
        container = TextContainer.all_text_entries[i]
        container.update()
        sidebar.blit(container, (0, i*(padding+text_container_height)))

    sidebar.blit(new_expr, new_expr.pos)
    main_surface.blit(toggle_button, toggle_button.pos)
    pygame.display.update()

pygame.quit()


# really need to complete reinitialising
# the steps are
# supply text to fraction (initially or once object has been created)
# get bounding box for text
# re-initialise the surface by calling pygame.Surface.__init__ with the new bounds
# render the new text and blit to the surface of the object
