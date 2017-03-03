from EventManager import EventManager
from TextContainer import TextContainer
from Fraction import Fraction
import pygame.freetype
from sympy import *

x = symbols('x')

pygame.freetype.init()

screen_width = 1280
screen_height = 720
main_surface = pygame.display.set_mode((screen_width, screen_height))

event_manager = EventManager()

my_text_container = TextContainer(event_manager)
my_fraction = Fraction(event_manager, 40, 22, 7)

while not event_manager.has_quit:

    event_manager.clock.tick(60)
    event_manager.update()

    main_surface.blit(my_fraction)

    pygame.display.update()

pygame.quit()


# really need to complete reinitialising
# the steps are
# supply text to fraction (initially or once object has been created)
# get bounding box for text
# re-initialise the surface by calling pygame.Surface.__init__ with the new bounds
# render the new text and blit to the surface of the object
