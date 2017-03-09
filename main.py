from EventManager import EventManager
import pygame
from TextContainer import TextContainer
import pygame.freetype


screen_width = 1280
screen_height = 720
main_surface = pygame.display.set_mode((screen_width, screen_height))

event_manager = EventManager()

text_container = TextContainer(event_manager, font_size=30, size=(400, 100))

while not event_manager.has_quit:

    event_manager.clock.tick(60)
    event_manager.update()
    main_surface.fill(pygame.Color('#461763'))

    text_container.update()

    main_surface.blit(text_container, (0, 0))
    pygame.display.update()

pygame.quit()


# really need to complete reinitialising
# the steps are
# supply text to fraction (initially or once object has been created)
# get bounding box for text
# re-initialise the surface by calling pygame.Surface.__init__ with the new bounds
# render the new text and blit to the surface of the object
