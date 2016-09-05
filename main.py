import pygame
from pygame.locals import *
from Button import Button
from Sidebar import Sidebar

screen_width = 1280
screen_height = 720
main_surface = pygame.display.set_mode((screen_width, screen_height), HWSURFACE)

mouse = None

my_sidebar = Sidebar((250, screen_height), pygame.Color('#30556c'), pygame.Color('#7c7a7a'))

clock = pygame.time.Clock()

running = True
while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONUP or MOUSEBUTTONDOWN:
            mouse = event.type
    for button in Button.all_buttons:
        button.set_surface(mouse)
        main_surface.blit(button, button.pos)

    main_surface.fill((0, 0, 0))

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

    main_surface.blit(my_sidebar, (my_sidebar.x, 0))

    pygame.display.update()
    mouse = None
pygame.quit()
