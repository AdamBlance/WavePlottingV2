from EventManager import EventManager
from FunctionBox import FunctionBox
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

event_manager = EventManager()


def delete_input(index):
    TextContainer.all_text_entries.pop(index)
    Button.all_buttons.pop(index)

    for n in range(1, len(Button.all_buttons)):
        height = len(TextContainer.all_text_entries)*(text_container_height + padding)-50
        Button.all_buttons[n].pos = (Button.all_buttons[n].pos[0], height)


def create_new_text_container():
    if len(TextContainer.all_text_entries)-1 != max_cont:
        FunctionBox(event_manager, (300, 80), 30)

graph = Graph(event_manager, (0, 0), (screen_width, screen_height))
sidebar = Sidebar((300, screen_height), pygame.Color('#3a577b'), pygame.Color('#4d4d4d'))
toggle_button = ToggleButton(event_manager, (95, 25), [screen_width - 220, 30], 'degrees', 'radians')

new_expr = Button(event_manager, (25, screen_height - 60), pygame.Color(0, 200, 0), 'ADD NEW',
                  create_new_text_container, size=(90, 35), gui_object_blitted_to=sidebar)

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
                item.is_on = False
            TextContainer.all_text_entries[bounds].is_on = True

    try:
        graph.update()
    except TypeError or NameError:
        pass

    toggle_button.update()

    new_expr.update()

    main_surface.blit(graph, graph.pos)

    sidebar.update()

    for i in range(len(TextContainer.all_text_entries)):
        container = TextContainer.all_text_entries[i]
        if container.is_on:
            container.update()
        sidebar.blit(container, (0, i*(padding+text_container_height)))

    for thing in FunctionBox.all_function_boxes:
        thing.update()

    main_surface.blit(sidebar, sidebar.pos)
    sidebar.blit(new_expr, new_expr.pos)
    main_surface.blit(toggle_button, toggle_button.pos)
    pygame.display.update()

pygame.quit()
