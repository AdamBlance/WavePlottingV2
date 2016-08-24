from Button import *

my_button = Button((0, 0), (0, 180, 180), 'hello', print, 'you pressed the button')

screen_width = 1280
screen_height = 720
main_surface = pygame.display.set_mode((screen_width, screen_height), HWSURFACE)

mouse = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONUP or MOUSEBUTTONDOWN:
            mouse = event.type
    for button in Button.all_buttons:
        button.set_surface(mouse),
        main_surface.blit(button, button.pos)
        pygame.display.update()
    mouse = None
pygame.quit()
