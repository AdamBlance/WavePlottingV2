import pygame
import pygame.freetype

class Fraction(pygame.Surface):

    fraction_font = pygame.freetype.Font('media/DejaVuSans.ttf')

    def __init__(self, top='\u2612', bottom='\u2612'):

        self.numerator = top
        self.denominator = bottom
        self.size = None
        self.reinit_surface()
        self.render()

    def reinit_surface(self):
        top = self.fraction_font.get_rect(self.numerator)
        bottom = self.fraction_font.get_rect(self.denominator)

        if top > bottom:
            largest = top
        else:
            largest = bottom





        super().__init__()

    def render(self):
        pass