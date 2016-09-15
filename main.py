import pygame
from pygame.locals import *
from Button import Button
from Sidebar import Sidebar
from ToggleButton import ToggleButton

screen_width = 1280
screen_height = 720
main_surface = pygame.display.set_mode((screen_width, screen_height), HWSURFACE)

mouse = None

my_sidebar = Sidebar((250, screen_height), pygame.Color('#30556c'), pygame.Color('#7c7a7a'))
my_toggle_button = ToggleButton((200, 200), (200, 0, 0), (0, 200, 0), 'degrees', 'radians')
clock = pygame.time.Clock()
penis = False
running = True
while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONUP and MOUSEBUTTONDOWN:
            mouse = event.type
        elif event.type == KEYDOWN:
            penis = True
    for button in Button.all_buttons:
        button.set_surface(mouse)
        main_surface.blit(button, button.pos)

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

    if penis:
        my_toggle_button.turn_on()
        penis = False

    my_toggle_button.redraw_surface()

    main_surface.blit(my_toggle_button, my_toggle_button.pos)
    main_surface.blit(my_sidebar, (my_sidebar.x, 0))

    pygame.display.update()
    mouse = None
pygame.quit()
